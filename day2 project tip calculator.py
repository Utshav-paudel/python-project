#welcome note
print("Welcome to the tip calculator")
#entering total bill
total=float(input("What was the total bill ? $"))
#entering percentage of tip given
per=int(input("What percentage tip would you like to give? "))
#Inputing Number of people to split the bill
person=int(input("How many people to split the bill ?"))
#tip calculation
tip=(total*per)/100
#totalwith tip 
totalwithtip=tip+total
#perperson calculation by rounding it up to two decimal value
perperson=round(totalwithtip/person,2)
#printing person bill value
print(f"Each person should pay{perperson}")



