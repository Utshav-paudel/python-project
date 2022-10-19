#Entering the age
age=input("Enter your current age")
#calculation
yearleft=90-int(age)
monthleft=int(yearleft*12)
weekleft=int(yearleft*(12*4))
dayleft=int(yearleft*365)
#printing using f string
print(f"you have {yearleft} year left,{weekleft}week left,{monthleft}month left,{dayleft}day left")