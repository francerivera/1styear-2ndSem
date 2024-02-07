import datetime
import pytz
class student:
    def __init__(self, id_number: int, name: str, course: str):
        self.id_number = id_number
        self.name = name
        self.course = course
    def __str__(self):
        return f"Testing Student: {id_number} - {name} - {course}"
    def validate_info(self):
        if len(id_number) == 9 and name.replace(' ','').isalpha():
            print("Student information is valid.")
        else:
            print("Student information is not valid.")

user = input("Testing Student: ").split(" - ")
profile = student(int(user[0]), user[1], user[2])
