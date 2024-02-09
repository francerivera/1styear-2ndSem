import datetime
import pytz
class Student:
    def __init__(self, id_number: int, name: str, course: str):
        self.id_number = id_number
        self.name = name
        self.course = course
        
    def __str__(self) -> str:
        return f"{self.id_number} - {self.self.name} - {self.course}"
        
    def validate_info(self) -> None:
        if len(str(self.id_number)) == 9 and self.name.replace(' ','').isalpha():
            print("Student information is valid.")
        else:
            print("Student information is not valid.")

try:
    user = input("Testing Student: ").split(" - ")
    profile = Student(int(user[0]), user[1], user[2])
    profile.validate_info()

    ph_timezone = pytz.timezone('Asia/Manila')
    time_in_ph = datetime.datetime.now(ph_timezone)
    print(time_in_ph.strftime(format = "%B %d, %Y  %H:%M"))
except:
    print("Please follow the format.")
