import json
import os

DATA_FILE = 'data/gradebook.json'

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": [], "courses": [], "enrollments": []}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Data file is corrupted. Starting with an empty gradebook.")
        return {"students": [], "courses": [], "enrollments": []}