import duckdb
import os

DB_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "dev.duckdb")
)

conn = duckdb.connect(DB_PATH)

print("\n📊 INCIDENTS COUNT:")
print(conn.execute("SELECT COUNT(*) FROM incidents").fetchall())

print("\n🎫 TICKETS COUNT:")
print(conn.execute("SELECT COUNT(*) FROM tickets").fetchall())

print("\n📌 SAMPLE INCIDENT:")
print(conn.execute("SELECT * FROM incidents LIMIT 1").fetchall())

print("\n📌 SAMPLE TICKET:")
print(conn.execute("SELECT * FROM tickets LIMIT 1").fetchall())