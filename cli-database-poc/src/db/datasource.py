from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent
filename = "datasource.json"
json_path = BASE_DIR / "resources" / filename


def create_datasource_if_not_exists():
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump({}, f, indent=4)
        
        print(f'Datasource {json_path} created!')


def get_or_create_datasource():
    create_datasource_if_not_exists()
    
    data = None
    with open(json_path, "r") as f:
        data = json.load(f)
    print(f'Datasource {json_path} loaded!')
    return data


def update_datasource(data: dict):
    create_datasource_if_not_exists()

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f'Datasource {json_path} updated!')
