from re import T


yourname=input("Enter your name")
lovername=input("Enter your lover name")
lower_yourname=yourname.lower()
lower_lovername=lovername.lower()
t=lower_yourname.count("t")
r=lower_yourname.count("r")
u=lower_yourname.count("u")
e=lower_yourname.count("e")
true=t+r+u+e
l=lower_yourname.count("l")
o=lower_yourname.count("o")
v=lower_yourname.count("v")
e=lower_yourname.count("e")
love=l+o+v+e
lovescore=str(true)+str(love)
lovescore=int(lovescore)
if (lovescore<10)and(lovescore>90):
    print("your relationship is like coke and mentos")
elif(lovescore>40) and (lovescore<50):
    print("you are great together")
else:
    print(f"your lovescore is {lovescore}")


