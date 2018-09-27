#QUESTION-1
year=int(input("Enter a year:- "))
if(year%4)==0:
   if(year%100)==0:
       if(year%400)==0:
           print("It is a leap year")
       else:
           print("It is not a leap year")
   else:
       print("It is a leap year")
else:
   print("It is not a leap year")


#QUESTION-2
length=int(input("Enter the length:- "))
breadth=int(input("Enter the breadth:- "))
if(length==breadth):
    print("It is a square")
else:
    print("It is a rectangle")


#QUESTION-3
list1=[]
for i in range(3):
    list1.append(int(input("Enter the age:- ")))
print("youngest person's age",min(list1))
print("oldest person's age",max(list1))


#QUESTION-4
age=int(input("Enter the age:- "))
sex = 'U'
while (sex != 'M' and sex != 'F') :
   sex=input("Enter sex (M or F):- ")

maritalstatus = 'U'
while (maritalstatus != 'Y' and maritalstatus != 'N') :
   maritalstatus=input("Enter marital status(Y or N):- ")
   
if(sex=='F'):
    print("She will have to work in urban areas only.")
elif(sex=='M' and age>=20 and age<=40):
    print("He can work anywhere.")
elif(sex=='M' and age>=40 and age<=60):
    print("He will work in urban ares only.")
else:
    print("ERROR")


#QUESTION-5
quantity=int(input("Enter the quantity:- "))
totalcost=quantity*100
if(totalcost>1000):
    totalcost=totalcost*0.1
print("Total cost is:- ",totalcost)
