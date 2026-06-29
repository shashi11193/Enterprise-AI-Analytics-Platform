import json
import os
from ingestion.config import JSON_DIR


def load_json_multiple_arrays(file_name: str):
    path = os.path.join(JSON_DIR, file_name)

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Split multiple JSON arrays safely
    chunks = raw.strip().split("]\n[")
    
    cleaned = []

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()

        if i != 0:
            chunk = "[" + chunk
        if i != len(chunks) - 1:
            chunk = chunk + "]"

        cleaned.extend(json.loads(chunk))

    return cleaned


def load_incidents():
    return load_json_multiple_arrays("incidents.json")


def load_tickets():
    return load_json_multiple_arrays("tickets.json")