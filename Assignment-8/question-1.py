#QUESTION-1
pie=3.14
class circle:
    def __init__(self,radius):
        self.rad=radius
    def getArea(self):
        return pie*self.rad*self.rad
    def getCircumference(self):
        return 2*pie*self.rad

cal=circle(int(input("enter the radius of circle:- ")))
print("area of circle:- ",cal.getArea())
print("circumference of the circle:- ",cal.getCircumference())
