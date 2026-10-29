# Dimensional Modeling (Star and Snowflake schema)

Dimensional modeling is a data warehouse design technique that organizes data into facts and dimensions
to make it easy to retrieve and analyze.

# Key Components

# Component | Description | Example

1. Fact table | Stores numeric, measurable data (metrics) | Sales amount, quantity, revenue
2. Dimension Table | Stores descriptive attributes that describe the facts. | Customer name, product category, branch, date
3. Primary Key | Unique ID for each record in a table | customer_id, product_id
4. Foreign Key | Connect fact table to a dimension table | fact_transaction.customer_id -> dim_customer.customer_id

# Why Use Dimensional Modeling

# Business Need | How Dimensional Modeling Helps

1 Fast queries for reports | joins are optimized and easy
2 Simple understanding for analysts | Business-friendly structure
3 Consistent data across teams | Shared dimension tables (like dim_date)
4 flexible expansion | you can add new dimensions or facts easily

# Star Schema

A Star Schema is a denormalized schema in which a central fact table stores quantitative business data and it is surrounded by
multiple dimension tables that store descriptive related to those facts. This structure simplifies analytical queries and improves
performance for business intelligence and reporting.
