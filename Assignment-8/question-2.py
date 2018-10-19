class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("name of the student:- ",self.name)
        print("roll no. of the student:- ",self.rollno)
        print("age of the student:- ",self.age)
        print("marks of the student:- ",self.marks)


student=student(input("enter the name of student:- "),int(input("enter the roll no.:- ")))
student.setAge(int(input("enter the age of student:- ")))
student.setMarks(int(input("enter the marks of student:- ")))
student.display()
