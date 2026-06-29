import yaml
import os
from ingestion.config import YAML_DIR


def load_yaml(file_name: str):
    path = os.path.join(YAML_DIR, file_name)

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_policies():
    return load_yaml("ai_policies.yaml")