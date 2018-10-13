#QUESTION-1
dictionary={input("Enter the key:- "):input("Enter the value:- ") for i in range(int(input("Enter the number of keys:- ")))}
for i in dictionary.keys():
    print(i)


#QUESTION-2
dictionary1={}
number=int(input("Enter the no of students:- "))
for i in range(number):
    a=input("Enter the name of student:- ")
    dictionary1[a]={input("Enter subject:- "):int(input("Enter the marks:- ")) for j in range(5)}
b=input("Enter the name of student to display their marks:- ")
for i,j in dictionary1.items():
    if(i==b):
        print("student has been found.")
        print("marks of the student:- ",j)
    else:
        print("student is not in the data.")
