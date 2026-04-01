class Student:
    def __init__(self, id, name):
        if not id or not name:
            raise ValueError("Student ID and name cannot be empty.")
        self.id=id
        self.name=name
    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name})"
class Course:
    def __init__(self, code, title):
        if not code or not title:
            raise ValueError("Course code and title cannot be empty.")
        self.code=code
        self.title=title
    def __str__(self):
        return f"Course)Code: {self.code}, Title: {self.title})"
    


class Enrollment:
    def init__(self, student_id, course_code, grades:list):
        if not student_id or not course_code:
            raise ValueError("Student ID and course code cannot be empty.")
        self.student_id=student_id
        self.course_code=course_code
        self.grades=grades if grades is not None else []

        for grade in self.grades:
            if not isinstance(grade, (int, float)) or not (0<=grade <=100):
                raise ValueError("Invalid grade value: {}. Grades must be numbers between 0 and 100.")
    def __str__(self):
        return f"Enrollment(Student ID: {self.student_id}, Course Code: {self.course_code}, Grades: {self.grades})"