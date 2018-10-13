#QUESTION-1
import re
email=input("enter your text:- ")
find=r"[a-zA-Z0-9-_.]+@[a-zA-Z-_.]+[a-zA-Z]"
print(re.findall(find,email))


#QUESTION-2
import re
i=input("enter the text:- ")
find=r"[+]{1}91-[6-9]{1}\d{9}"
print(re.findall(find,i))
