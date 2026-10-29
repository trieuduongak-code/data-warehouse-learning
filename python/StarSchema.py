import pandas as pd 
import sqlite3
from pathlib import Path
import os 
df= pd.read_csv(r"D:\DataEngineering\data-warehouse-learning\data\transactions_2025.csv")

project_dir = Path(r"D:\DataEngineering\data-warehouse-learning")
csv_path = project_dir / "data" / "transactions_2025.csv"
db_path = project_dir / "local_warehouse.db"

# Transform 
df["timestamp"]= pd.to_datetime(df["timestamp"])
df= df[df["status"] == "Success"]
df["date"]= df["timestamp"].dt.date

os.makedirs(project_dir, exist_ok= True)

with sqlite3.connect(db_path) as conn:
    df.to_sql(
        "fact_transactions",
        conn,
        if_exists="replace",
        index=False
    )
    print("Data loaded into fact_transactions table")
    query = """
    SELECT
        branch,
        strftime('%Y-%m', timestamp) AS month,
        SUM(amount) AS total_amount,
        COUNT(*) AS txn_count
    FROM fact_transactions
    GROUP BY
        branch,
        strftime('%Y-%m', timestamp)
    ORDER BY month DESC;
    """

    result = pd.read_sql_query(query, conn)

