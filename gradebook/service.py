from .storage import load_data, save_data #relative import for better modularity
import uuid

def parse_grade(grade_input): 
    #Grade validation and parsing logic
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        raise ValueError("Grade must be between 0 and 100.")
    except (ValueError, TypeError):
        raise ValueError("Invalid grade input. Please enter a number between 0 and 100.")

def _get_all():
    # Internal function to load all data. This is used by other service functions to ensure they always work with the latest data.
    return load_data()

def add_student(name):
    #Generate a unique ID for the student and save it to the data store
    data = _get_all()
    new_id = str(uuid.uuid4())[:8]
    data.append({"type": "student", "id": new_id, "name": name})
    save_data(data)
    return new_id

def list_students():
    #List all students sorted alphabetically by name
    data = _get_all()
    students = [item for item in data if item["type"] == "student"]
    return sorted(students, key=lambda s: s["name"])

def add_course(code, title):
    #Add a new course to the data store
    data = _get_all()
    data.append({"type": "course", "code": code, "title": title})
    save_data(data)

def add_grade(student_id, course_code, grade):
    #Add a grade for a specific student and course. This function will find the corresponding enrollment and update the grades list.
    data = _get_all()
    enrollment = next((e for e in data if e["type"] == "enrollment" 
                      and e["student_id"] == student_id 
                      and e["course_code"] == course_code), None)
    if enrollment:
        enrollment["grades"].append(grade)
    save_data(data)

def compute_average(student_id, course_code):
    #Average grade for a specific student in a specific course
    data = _get_all()
    enrollment = next((e for e in data if e["type"] == "enrollment" 
                      and e["student_id"] == student_id 
                      and e["course_code"] == course_code), None)
    if enrollment and enrollment["grades"]:
        return sum(enrollment["grades"]) / len(enrollment["grades"])
    return 0.0

def compute_gpa(student_id):
    #Calculate the overall GPA for a student
    data = _get_all()
    student_enrollments = [e for e in data if e["type"] == "enrollment" 
                          and e["student_id"] == student_id]
    averages = [compute_average(student_id, e["course_code"]) for e in student_enrollments]
    if averages:
        return sum(averages) / len(averages)
    return 0.0

def enroll(student_id, course_code):
    #Enroll a student in a course by creating an enrollment record with an empty grades list
    data = _get_all()
    data.append({"type": "enrollment", "student_id": student_id, "course_code": course_code, "grades": []})
    save_data(data)

def list_courses():
    #List all courses sorted by course code
    data = _get_all()
    courses = [item for item in data if item["type"] == "course"]
    return sorted(courses, key=lambda c: c["code"])

def list_enrollments():
    #List all enrollment records
    data = _get_all()
    return [item for item in data if item["type"] == "enrollment"]