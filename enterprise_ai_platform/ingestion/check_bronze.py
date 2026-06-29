import duckdb
from ingestion.config import WAREHOUSE_PATH

conn = duckdb.connect(WAREHOUSE_PATH)

print("\n=== TABLES ===")
print(conn.execute("SHOW TABLES").fetchall())

print("\n=== INCIDENTS COUNT ===")
print(conn.execute(
    "SELECT COUNT(*) FROM incidents"
).fetchall())

print("\n=== TICKETS COUNT ===")
print(conn.execute(
    "SELECT COUNT(*) FROM tickets"
).fetchall())

print("\n=== SAMPLE INCIDENTS ===")
print(conn.execute(
    "SELECT * FROM incidents LIMIT 5"
).fetchdf())

print("\n=== SAMPLE TICKETS ===")
print(conn.execute(
    "SELECT * FROM tickets LIMIT 5"
).fetchdf())

conn.close()