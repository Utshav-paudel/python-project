score=input("Enter your score in all subject")
scorelist=score.split()
highscore=scorelist[0]
for score in scorelist:
    if score>highscore:
        highscore=score
print(f"Highest score is {highscore}")