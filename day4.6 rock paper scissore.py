# Rock Paper Scissors ASCII Art

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
choice=int(input("Enter 0 for rock 1 for paper and 2 for scissors"))
print("YOU:")
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
else:
    print(scissors)
#for computer 
choice_computer=random.randint(0,2)
print("COMPUTER:")
if choice_computer==0:
    print(rock)
elif choice_computer==1:
    print(paper)
else:
    print(scissors)
if (choice==0)and (choice_computer==1):
    print("You lose")
if(choice==1)and(choice_computer==0):
    print("You win")
if(choice==1)and(choice_computer==2):
    print("You lose")
if(choice==2)and(choice_computer==1):
    print("You won")
if(choice==0)and(choice_computer==2):
    print("You won")
if(choice==2)and(choice_computer==0):
    print("You lose")
if(choice==choice_computer):
    print("Draw")
