# Data Warehouse is a central system that stores clean, structured and historical data from multiple sources

# optimized for analytics and decision-making.

# THE 4 CLASSIC CHARACTERISTICS

# Feature | Meaning | Examples

# 1 subject-oriented | focus on business subjects like sales, customers, transactions |All customers-related data stored together

# 2 Integrated | Combining multiple systems with consistent naming and formats | Merge data from mySQL, CRM and Logs

# 3 Time-variant | keeps historical data for trend analysis | Compare jan 2024 with jan 2025 deposits

# 4 Non-Volatile | Data isn't overwritten, only appended | Transactions from 2019 still stored

# OLTP AND OLAP - CLARIFYING THE DIFFERENCE

# Aspect | OLTP(Operational) | OLAP(Analytical/ Warehouse)

# 1 Goal | Run day-to-day business | Analyze and Report

# 2 Users | Cashiers, Apps | Analysts, Management

# 3 Data sizes | small / current | Large / historical

# 4 Queries | Insert, Update | Aggregate, summarize

# 5 Examples | ATM processing 5000 withdrawal | Dashboard showing total deposits per

## Core Components

1. **Source Systems** – Where raw data originates (databases, CRMs, sensors).

2. **Staging Layer** – Temporary zone for raw data before cleaning.

3. **ETL/ELT Process** – Scripts or jobs (Python, Airflow, Spark) that transform data.

4. **Data Warehouse Storage** – Columnar storage optimized for analytics (e.g., Redshift, BigQuery).

5. **BI Layer** – Visualization and reporting tools (Power BI, Looker, Tableau).

## Columnar Storage – Why It Matters

Warehouses store data by column rather than by row. That means if you run a query on only 3 columns out of 20, it physically reads just those three – far faster and cheaper. Columnar storage with compression is what gives warehouses their speed.
