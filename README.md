# Gradebook Management System

A Python-based CLI application designed to manage student enrollments, courses, and academic performance tracking.

## 🚀 Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv

2. **Activate the Virtual Environment:**
   * **Windows:** `venv\Scripts\activate`
   * **macOS/Linux:** `source venv/bin/activate`

## 🛠️ Usage

### 1. Seed the Database
Before running the app, populate it with initial sample data (students, courses, and enrollments):
```bash
python scripts/seed.py

### 2. Run the Application
Launch the main Command Line Interface:
```bash
python main.py
```text
Select an option:
1. Add Student
2. List Students
Choice: 2

--- Student List ---
1. Valera Gashi (ID: 8a2f1b3c)
2. Feri Gashi (ID: 4d9e7a2b)
3. Vesa Gashi (ID: 1c5d9f0e)

### 3. Run Unit Tests
To verify the system logic:
```bash
export PYTHONPATH=.
python -m unittest tests/test_service.py

## 🧠 Design Decisions & Limitations

### Design Decisions
* **JSON-Based Storage:** I used a JSON file for data persistence because it is lightweight and allows the gradebook to save between sessions without needing a complex database setup.
* **Modular Architecture:** The project is divided into `service.py`, `storage.py`, and `models.py` to keep the code organized and easy to update.
* **Unique IDs:** I implemented `uuid` to give every student a unique ID, preventing confusion if two students have the same name.

### Limitations
* **Local Environment:** The system is built for a single user on a local machine and doesn't support multiple people editing at the same time.
* **CLI Only:** This is a terminal-based app and does not have a visual window or web interface.
