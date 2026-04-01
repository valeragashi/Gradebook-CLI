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

