
class Student:
    def __init__(self,rollno,name):
        self.rollno = rollno;
        self.name = name;
    
    def printing(self):
        print(f"rollno : {self.rollno} name :{self.name} ")
        

shubham = Student(1,'shubham')

if __name__ == '__main__':
    print(shubham.printing())