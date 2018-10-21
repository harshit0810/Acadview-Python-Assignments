#QUESTION-1
file=open("file.txt","r")
n=int(input("enter the no. of lines:- "))
print(file.readlines()[0:n])



#QUESTION-2
file1=open("file.txt","r")
line=input("enter the string:- ")
n=file1.read()
count=n.count(line)
print(count)


#QUESTION-3
file1=open("file.txt","r")
file2=open("file1.txt","w+")
n=file1.readlines()
file2.writelines(n)

file1.close()
file2.close()
file2=open("file1.txt","r")
print(file2.read())



#QUESTION-4
file1=open("file.txt","r")
file2=open("file1.txt","r")
a=file1.readlines()
b=file2.readlines()
file1.close()
file2.close()
x=list(zip(a,b))
print(x)
file3=open("file3.txt","w")
for i in x:
    for j in i:
        file3.write(j)
file3.close()



#QUESTION-5
import random
file1=open('file4.txt','w')
for i in range(1,10):
    file1.writelines(str(random.randrange(1,1000))+'\n')
file1.close()
file1=open('file4.txt','r')
file_content=file1.readlines()
file1.close()
file1=open('file4.txt','w')
sorting=[]
for i in file_content:
    sorting.append(int(i.strip()))
sorting.sort()
sorting=[str(i) for i in sorting]
file1.writelines('\n'.join(sorting))
file1.close()
