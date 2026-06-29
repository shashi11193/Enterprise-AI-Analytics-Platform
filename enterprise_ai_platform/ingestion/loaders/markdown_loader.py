import os
from ingestion.config import MD_DIR


def load_markdown(file_name: str):
    path = os.path.join(MD_DIR, file_name)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_all_markdown():
    docs = {}

    for file in os.listdir(MD_DIR):
        if file.endswith(".md"):
            docs[file] = load_markdown(file)

    return docs