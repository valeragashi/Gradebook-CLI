import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gradebook import service
from gradebook.storage import save_data

def seed_data():
    print("Resetting and seeding data...")

    save_data({"students": [], "courses": [], "enrollments": []})
               
    s1_id = service.add_student("Valera Gashi")
    s2_id = service.add_student("Feri Gashi")
    s3_id = service.add_student("Vesa Gashi")

    service.add_course("CS101", "Intro to Computer Science")
    service.add_course("MATH101", "Intro to Mathematics")

    service.enroll(s1_id, "CS101")
    service.enroll(s1_id, "MATH101")
    service.enroll(s2_id, "CS101")

    print("Seeding complete.")
if __name__ == "__main__":
    seed_data()
