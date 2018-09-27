#QUESTION-1
pie=3.14
def area(radius):
    print("Area of sphere:- ",4*pie*radius**2)
radius1=int(input("Enter radius of sphere:- "))
area(radius1)


#QUESTION-2
def perfect(n):
    shu=0
    for i in range(1,n):
        if(n%i==0):
            shu=shu+i
    if (shu==n and n!=0):
        return True
    else:
        return False
for i in range(100):
    ans=perfect(i)
    if(ans==True):
        print("perfect number:- ",i)


#QUESTION-3
num=int(input("Enter the number:- "))
for i in range(1,10):
    print(num,"x",i,"=",num*i)


#QUESTION-4
def calculate(x,y):
    if(y==1):
        return number
    if(y!=1):
        return(number*calculate(number,y-1))
    
number=int(input("Enter the number:- "))
power=int(input("Enter power:- "))
print(calculate(number,power))
