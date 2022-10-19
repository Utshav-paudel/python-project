weight=float(input("Enter the weight in kg "))
height=float(input("Enter the height in m "))
BMI=weight/height**2
if BMI<18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI<25:
    print(f"Your BMI is {BMI} and you are normal")
elif BMI==25:
    print(f"Your BMI is {BMI} and you are overweight")
else:
    print(f"Your BMI is {BMI} and you are obessed")
    
