# 4.1 BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Ooutput: Obesity")
elif 25 <= bmi < 30:
    print("Output: Overweight")
elif 18.5 <= bmi < 25:
    print("Output: Normal")
else:
    print("Output: Underweight")