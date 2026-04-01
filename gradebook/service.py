from .storage import load_data, save_data
import uuid

def parse_grade(grade_input):
    """Validates and converts grade input to a float (0-100)."""
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        raise ValueError("Grade must be between 0 and 100.")
    except (ValueError, TypeError):
        raise ValueError("Invalid grade input. Please enter a number between 0 and 100.")

def _get_all():
    """Helper function to retrieve the full data dictionary."""
    return load_data()

def add_student(name):
    """Adds a new student and returns their generated short ID."""
    data = _get_all()
    new_id = str(uuid.uuid4())[:8]
    data["students"].append({"id": new_id, "name": name})
    save_data(data)
    return new_id

def list_students():
    """Returns a list of all students sorted by name."""
    data = _get_all()
    return sorted(data["students"], key=lambda s: s["name"])

def add_course(code, title):
    """Registers a new course in the system."""
    data = _get_all()
    data["courses"].append({"code": code, "title": title})
    save_data(data)

def list_courses():
    """Returns a list of all courses sorted by code."""
    data = _get_all()
    return sorted(data["courses"], key=lambda c: c["code"])

def enroll(student_id, course_code):
    """Enrolls a student into a specific course."""
    data = _get_all()
    data["enrollments"].append({
        "student_id": student_id, 
        "course_code": course_code, 
        "grades": []
    })
    save_data(data)

def add_grade(student_id, course_code, grade):
    """Adds a numeric grade to a student's specific course enrollment."""
    data = _get_all()
    enrollment = next((e for e in data["enrollments"] 
                      if e["student_id"] == student_id 
                      and e["course_code"] == course_code), None)
    if enrollment:
        enrollment["grades"].append(grade)
    save_data(data)

def compute_average(student_id, course_code):
    """Calculates average grade for a student in a specific course."""
    data = _get_all()
    enrollment = next((e for e in data["enrollments"] 
                      if e["student_id"] == student_id 
                      and e["course_code"] == course_code), None)
    if enrollment and enrollment["grades"]:
        return sum(enrollment["grades"]) / len(enrollment["grades"])
    return 0.0

def compute_gpa(student_id):
    """Calculates student GPA across all enrolled courses."""
    data = _get_all()
    student_enrollments = [e for e in data["enrollments"] 
                          if e["student_id"] == student_id]
    
    averages = []
    for e in student_enrollments:
        avg = compute_average(student_id, e["course_code"])
        averages.append(avg)

    if averages:
        return sum(averages) / len(averages)
    return 0.0

def list_enrollments():
    """Returns a list of all enrollment records."""
    data = _get_all()
    return data["enrollments"]

