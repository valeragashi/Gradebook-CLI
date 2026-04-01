from gradebook.storage import save_data, load_data
import uuid

#task 6
def parse_grade(grade_input):
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        else:
            raise ValueError("Grade must be between 0 and 100.")
    except (ValueError, TypeError):
        raise ValueError("Invalid grade input. Please enter a number between 0 and 100.")
def _get_all():
    return load_data()
def add_student(name):
    data = _get_all()
    new_id = str(uuid.uuid4())[:8] # Generate a short unique ID
    data.append({"type": "student", "id": new_id, "name": name})
    save_data(data)
    return new_id
def list_students():
    data = _get_all()
    students = [item for item in data if item["type"] == "student"]
    return sorted(students, key=lambda s: s["name"])

def add_course(code, title):
    data = _get_all()
    data.append({"type": "course", "code": code, "title": title})
    save_data(data)

def add_grade(student_id, course_code, grade):
    data = _get_all()
    enrollment = next((e for e in data if e["type"] == "enrollment" and e["student_id"] == student_id and e["course_code"] == course_code), None)

    if enrollment:
        enrollment["grades"].append(grade)
    save_data(data)
def compute_average(student_id, course_code):
    data = _get_all()
    enrollment = next((e for e in data if e["type"] == "enrollment" and e["student_id"] == student_id and e["course_code"] == course_code), None)

    if enrollment and enrollment["grades"]:
        return sum(enrollment["grades"]) / len(enrollment["grades"])
    return 0.0

def compute_gpa(student_id):
    data = _get_all()
    enrollment = next((e for e in data if e["type"] == "enrollment" and e["student_id"] == student_id), None)
    if enrollment and enrollment["grades"]:
        return sum(enrollment["grades"]) / len(enrollment["grades"])
    return 0.0
def compute_gpa(student_id):
    data = _get_all()
    student_enrollments = [e for e in data if e["type"] == "enrollment" and e["student_id"] == student_id]
    averages= [compute_average(student_id, e["course_code"]) for e in student_enrollments]

    if averages:
        return sum(averages) / len(averages)
    return 0.0

def enroll(student_id, course_code):
    data = _get_all()
    data.append({"type": "enrollment", "student_id": student_id, "course_code": course_code, "grades": []})
    save_data(data)
def list_courses():
    data= _get_all()
    courses = [item for item in data if item["type"] == "course"]
    return sorted(courses, key=lambda c: c["code"])

def list_enrollments():
    data= _get_all()
    return [item for item in data if item["type"] == "enrollment"]