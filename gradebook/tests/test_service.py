import unittest
from gradebook import service

class TestGradebookService(unittest.TestCase):
    
     #setup: clear data file before each test
    def test_add_student_happy_path(self):
        student_name = "Valera"
        student_id = service.add_student(student_name)
        self.assertIsNotNone(student_id)
        self.assertEqual(len(student_id), 8)  # Check if ID is 8 characters long

    def test_add_grade_happy_path(self): #setup: add student, course, enroll, then add grade
        s_id = service.add_student("Feri")
        service.add_course("CS101", "Intro to CS")
        service.enroll(s_id, "CS101")

        service.add_grade(s_id, "CS101", 95)
        avg = service.compute_average(s_id, "CS101")
        self.assertEqual(avg, 95)

    def test_compute_gpa_happy_path(self): #setup: add student, courses, enroll, add grades, then compute GPA
        s_id = service.add_student("Geri")
        service.add_course("CS101", "Intro to CS")
        service.add_course("MATH101", "Intro to Math")
        service.enroll(s_id, "CS101")
        service.enroll(s_id, "MATH101")

        service.add_grade(s_id, "CS101", 90)
        service.add_grade(s_id, "MATH101", 80)

        gpa = service.compute_gpa(s_id)
        self.assertEqual(gpa, 85)

    def test_compute_average_edge_case_no_grades(self):
        avg= service.compute_average("nonexistent_student", "nonexistent_course")
        self.assertEqual(avg, 0.0)

    def setUp(self):
        from gradebook.storage import save_data
        save_data({"students": [], "courses": [], "enrollments": []})

if __name__ == '__main__':
    unittest.main()