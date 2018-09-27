#QUESTION-1
list1=[int(input("Enter the number:- ")) for i in range(10)]
for i in list1:
    print(i)

    
#QUESTION-2
while(True):
    print("infinite loop")


#QUESTION-3
number=int(input("Enter the number of elements:- "))
list2=[int(input("Enter number:- ")) for i in range(number)]
list3=[i**2 for i in list2]
print(list3)


#QUESTION-4
list4=[1,'jon',11.45235,'snow',87,24,24.324]
slist=[]
flist=[]
ilist=[]
for i in list4:
    if(type(i)==float):
        flist.append(i)
    elif(type(i)==int):
        ilist.append(i)
    elif(type(i)==str):
        slist.append(i)
print(slist)
print(flist)
print(ilist)


#QUESTION-5
list5=[int(i) for i in range(1,101)]
list6=[]
for i in list5:
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        if(i!=1):
            list6.append(i)
print("all prime numbers:- ",list6)


#QUESTION-6
for i in range(4):
    for j in range(i+1):
        print("*",end='')
    print()


#QUESTION-7
list7=[int(input("Enter the no.:- ")) for i in range(int(input("Enter the no. of elements:- ")))]
number=int(input("Enter the no. for search and delete:- "))
for i in list7:
    if(number in list7):
        list7.remove(number)
        print("no. deleted")
        print("last list",list7)
        break
else:
    print("no. not available")

