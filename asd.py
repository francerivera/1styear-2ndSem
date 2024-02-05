class student:
    def __init__(self,id_number: int,name: str,course: str) -> str:
        self.id_number = id_number
        self.name = name
        self.course = course
        
id_number = input("ID Number: ")
name = str(input("Name: "))   
course = str(input("Course: "))

def introduce(self):
    print(f"Testing Student: {id_number} - {name} - {course}")
        
def validate_info() -> None:
    if len(id_number) == 9 and name.isalpha:
        print ("Student information is valid.")
    else:
        print("Student information is not valid.")

validate_info()
