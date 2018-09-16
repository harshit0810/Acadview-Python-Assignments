#QUESTION-1
list1=[23,34,553,542]
print(list1[::-1])


#QUESTION-2
string1='Game Of Thrones'
for i in string1:
    if(i.isupper()):
        print(i,end=' ')

print()
#QUESTION-3
string2=input("Enter the list:- ")
string2=string2.split(',')
list2=[]
for i in string2:
    list2.append(int(i))
print(list2)


#QUESTION-4
string3=input("Enter string:- ")
if(string3==string3[::-1]):
    print("Palindromic no.")
else:
    print("Not Palindromic no.")


#QUESTION-5
import copy
li1 = [1,2,[3,5],4]
li2 = copy.copy(li1) 
print ("The original elements before shallow copying") 
for i in range(0,len(li1)): 
    print (li1[i],end=" ") 
  
print("\r")  
li2[2][0] = 7 
print ("The original elements after shallow copying") 
for i in range(0,len( li1)): 
    print (li1[i],end=" ") 
