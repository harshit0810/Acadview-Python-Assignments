#QUESTION-1
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("no. !/0")


#QUESTION-2
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("list out of index.")


#QUESTION-3
#Output will be {An exception} as "hi there" will not be found.


#QUESTION-4
#smjh nhi aaya


#QUESTION-5
#IMPORT ERROR
try:
    import date
except ImportError:
    print("import error")
    
 #INDEX ERROR   
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index error")
    
 #VALUE ERROR   
try:
    n=input("enter the integer:- ")
    n=int(n)
except ValueError:
    print("value error")
else:    
    print("value is inserted.")

















    
