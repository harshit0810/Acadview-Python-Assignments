#QUESTION-1
list1=[]
abcd=int(input("enter the no. of elements:- "))
for i in range(abcd):
    list1.append(input("enter the element:- "))
print(list1)


#QUESTION-2
list2=['google','apple','facebook','microsoft','tesla']
list1+=list2
print(list1)


#QUESTION-3
list3=[1,1,1,3,2,2,6,7,4,4,3,5]
obj=input("Enter the no.:- ")
a=list3.count(int(obj))
print(a)


#QUESTION-4
list4=[22,55,332,435,255]
list4.sort()
print(list4)


#QUESTION-5
A=[1,5,7,9,25,65]
B=[23,35,52,56,68,545]
C=A+B
C.sort()
print(C)


#QUESTION-6
even=odd=0
for i in C:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Count of even no. is  ",even)
print("Count of odd no. is  ",odd)
