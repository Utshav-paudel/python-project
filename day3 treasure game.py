#treasure game created using conditional logic
#welcome to the game
print("Welcome to the treasure game ")
print("Lets find the treasure")
#firstmove to user
firstmove=input("Press l for left and r for right")
#converting to lowercase for eliminating case sensitive error
firstmove=firstmove.lower()
if firstmove=="l":
    print("congrats for moving forward")
    secondmove=input("enter s for swim and w for wait")
    secondmove=secondmove.lower()
    if secondmove=="w":
        print("Patient paid off you passed next level")
        thirdmove=input("choose Y for yellow B for blue and R for red door")
        thirdmove=thirdmove.lower()
        if thirdmove=="y":
            print("You caught fire game over")
        elif thirdmove=="b":
            print("You fell into sea game over")
        else:
            print("YOU WON")
    else:
        print("Shark has eaten you game over")
else:
    print("You fail game over")