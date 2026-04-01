import json
import os
import logging

#task 7 logging setup
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DATA_FILE = 'data/gradebook.json'

def save_data(data):
    """Saves data to JSON and logs the success."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info("Data saved successfully.")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        raise IOError("An error occurred while saving data.")

def load_data():
    """Loads data from JSON and logs the success before returning."""
    if not os.path.exists(DATA_FILE):
        logging.info("Data file not found. Initializing new gradebook.")
        return {"students": [], "courses": [], "enrollments": []}
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        # Log happens BEFORE the return
        logging.info("Data loaded successfully.")
        return data
    except json.JSONDecodeError:
        logging.error("Data file is corrupted. Starting with an empty gradebook.")
        print("Error: Data file is corrupted. Starting with an empty gradebook.")
        return {"students": [], "courses": [], "enrollments": []}