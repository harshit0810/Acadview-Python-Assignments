#QUESTION-7
class shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return self.l*self.b
class rectangle(shape):
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        super().__init__(self.l,self.b)
class square(shape):
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        super().__init__(self.l,self.b)
square=square(2,2)
rect=rectangle(10,20)
print("area of the square:- ",square.area())
print("area of the rectangle:- ",rect.area())

