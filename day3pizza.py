size=input("Enter the size of pizza S,M or L")
pepperoni=input("do you want pepperoni Y OR N")
Extra_cheese=input("do you want extra cheese Y or N")
price=0
if size=="S":
    price=15
    if pepperoni=="Y":
        price+=2
    print(f"price for small pizza is {price}")
elif size=="M":
    price=20
    if pepperoni=="Y":
        price+=3
    print(f"price for medium pizza is {price}")
elif size=="L":
    price=25
    if pepperoni=="Y":
        price+=3
    print(f"price for large pizza is {price}")

if Extra_cheese=="Y":
    price+=1
    print(f"Your bill is ${price}")