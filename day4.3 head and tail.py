import random
choice=int(input("Select 0 for Heads and 1 for Tails"))
result=random.randint(0,1)
if result==0:
    print("Heads")
else:
    print("Tails")
if result==choice:
    print("You won the toss")
else:
    print("You lost the toss")