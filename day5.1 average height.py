height=input("enter student heights separated by comma ")
heightlist=height.split(",")
totalheight=0
totalpeople=int(len(heightlist))

for heightli in heightlist:
    totalheight+=int(heightli)
average=totalheight/totalpeople
print(f"Average height of people is {average}")
