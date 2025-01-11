import duckdb
from config.config import MOTHERDUCK_TOKEN

def get_connection():
    return duckdb.connect(f"md:?token={MOTHERDUCK_TOKEN}")

def execute_query(query):
    conn = get_connection()
    return conn.execute(query).fetch_df()

def get_inventory_status():
    query = """
    SELECT 
        StockCode, 
        Description, 
        SUM(CAST(Quantity AS INTEGER)) AS TotalStock
    FROM my_db.main.data
    GROUP BY StockCode, Description
    ORDER BY TotalStock DESC;
    """
    return execute_query(query)

def get_sales_trends():
    query = """
    SELECT 
        Date, 
        SUM(CAST(Quantity AS INTEGER) * CAST(UnitPrice AS DOUBLE)) AS TotalSales
    FROM my_db.main.data
    GROUP BY Date
    ORDER BY Date ASC;
    """
    return execute_query(query)

def get_customer_insights():
    query = """
    SELECT 
        CustomerID, 
        SUM(CAST(Quantity AS INTEGER) * CAST(UnitPrice AS DOUBLE)) AS TotalSpend
    FROM my_db.main.data
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
    ORDER BY TotalSpend DESC
    LIMIT 10;
    """
    return execute_query(query)
