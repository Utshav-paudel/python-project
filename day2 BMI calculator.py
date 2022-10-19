#Entering of input and output
weight=input("Enter your weight in kg")
height=input("Enter your height in meter")
#since height and weight may have fractional part float data type is used
weight=float(weight)
height=float(height)
#calculation of BMI
BMI=weight/(height**2)
#BMI print as integerA
print(int(BMI))