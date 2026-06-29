import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

RAW_DIR = os.path.join(BASE_DIR, "raw_sources")

JSON_DIR = os.path.join(RAW_DIR, "json")
YAML_DIR = os.path.join(RAW_DIR, "yaml")
MD_DIR = os.path.join(RAW_DIR, "markdown")
PDF_DIR = os.path.join(RAW_DIR, "pdfs")

WAREHOUSE_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "dev.duckdb")
)