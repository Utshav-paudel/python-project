#to use random module it is imported first
import random
#entering name
name=input("Enter everyone name separated by comma")
#list of string is formed using split function
separatename=name.split(",")
#It tell the number of element in list
numberofname=len(separatename)
#randome number is selected from 0 to 1 less because len count from 1  
randomnumber=random.randint(0,numberofname-1)
#random name is selected from list
randomname=separatename[randomnumber]
#print using f string
print(f"{randomname} will buy meal for everyone")
#another short method to print random name from list is using random.choice()
# print(random.choice(separatename))