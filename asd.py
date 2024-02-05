testing = str(input("Testing Student: "))


class student:
    def __init__(self,id_number: int,name: str,course: str) -> str:
        self.id_number = int(input("ID Number: "))
        self.name = str(input("Name: "))
        self.course = str(input("Course: "))
    
    def id_number(self):
        return self.id_number

    def name(self):
        return self.name
        
    def course(self):
        return self.course
    
    if len(testing) == 9:
        if testing.isalpha():
            print("Student information is valid.") 
        else:
            print("Student information is not valid.")
        
        
    def __str__(self):
        return f"{id_number} - {name} - {course}"
       
    
    def validate_info() -> None:
        
