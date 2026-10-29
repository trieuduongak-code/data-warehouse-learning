# Ex: which branch generated the highest total transaction amount per month?
import pandas as pd 
import sqlite3 
from pathlib import Path 

# Check connect with data base
project_dir= Path(__file__).resolve().parent.parent
db_path= project_dir / "data" / "local_warehouse.db"


# Load and Transform data from transaction.csv
df = pd.read_csv(r"D:\DataEngineering\data-warehouse-learning\data\transactions_2025_dimensionalModels.csv")
df["timestamp"]= pd.to_datetime(df["timestamp"])
df= df[df["status"] == "Success"]
df["date"]= df["timestamp"].dt.date

dim_branch= df[['branch']].drop_duplicates().reset_index(drop= True)
dim_branch['branch_id']= ['B'+ str(i+1).zfill(3) for i in range(len(dim_branch))]
dim_branch.rename(columns= {'branch':'branch_name'}, inplace= True)

dim_customer= df[['customer_id']].drop_duplicates().reset_index(drop= True)
dim_customer['customer_name']= 'Customer_'+ dim_customer.index.astype(str)

regions= ['Lagos', 'Abuja', 'Kano', 'Ibadan']*(len(dim_customer)//4+1)
regions= regions[:len(dim_customer)]
dim_customer['region']= regions

unique_dates= pd.to_datetime(df['date'].unique())
dim_date= pd.DataFrame(
    {
        'date_id': unique_dates.strftime('%D%Y%m%d'),
        'full_date': unique_dates
    }
)
dim_date['year']= pd.to_datetime(dim_date['full_date']).dt.year
dim_date['month']= pd.to_datetime(dim_date['full_date']).dt.strftime('%B')
dim_date['day']= pd.to_datetime(dim_date['full_date']).dt.day

fact_transactions= df.merge(dim_branch, left_on="branch", right_on="branch_name", how="left")
fact_transactions['date_id']= pd.to_datetime(fact_transactions['date']).dt.strftime('%D%Y%m%d')
fact_transactions= fact_transactions[['transaction_id', 'customer_id', 'branch_id', 'date_id', 'amount', 'transaction_type', 'status']]

with sqlite3.connect(db_path) as conn:
    dim_branch.to_sql("dim_branch", conn, if_exists="replace", index= False)
    dim_customer.to_sql("dim_customer", conn, if_exists="replace", index= False)
    dim_date.to_sql("dim_date", conn, if_exists="replace", index= False)
    fact_transactions.to_sql("fact_transactions", conn, if_exists= 'replace', index= False)
    
query = """
WITH monthly_sales AS (
    SELECT
        d.year,
        d.month,
        f.branch_id,
        SUM(f.amount) AS total_amount
    FROM fact_transactions AS f
    JOIN dim_date AS d
        ON f.date_id = d.date_id
    GROUP BY
        d.year,
        d.month,
        f.branch_id
),
ranked_sales AS (
    SELECT
        year,
        month,
        branch_id,
        total_amount,
        RANK() OVER (
            PARTITION BY year, month
            ORDER BY total_amount DESC
        ) AS sales_rank
    FROM monthly_sales
)
SELECT
    year,
    month,
    branch_id,
    total_amount
FROM ranked_sales
WHERE sales_rank = 1
ORDER BY year DESC, month;
"""

with sqlite3.connect(db_path) as conn:
    result = pd.read_sql_query(query, conn)

print(result)