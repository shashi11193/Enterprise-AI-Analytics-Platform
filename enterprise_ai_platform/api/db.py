import duckdb
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "..", "dev.duckdb")

def get_conn():
    return duckdb.connect(DB_PATH, read_only=True)