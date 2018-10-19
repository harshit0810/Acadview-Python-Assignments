#QUESTION-1
file=open("file.txt","r")
n=int(input("enter no. of lines:- "))
print(file.readlines()[0:n])
