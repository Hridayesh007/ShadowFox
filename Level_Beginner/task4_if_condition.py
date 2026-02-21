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

Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
#4.2 - Country Checker
city = input("Enter a city name: ")
if city in Australia:
    print(city,"is in Australia")
elif city in UAE:
    print(city,"is in UAE")
elif city in India:
    print(city,"is in India")

#4.3 - check if two cities belong to the same country
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
if city1 and city2 in Australia:
    print("Both cities are in Australia")
elif city1 and city2 in UAE:
    print("Both cities are in UAE")
elif city1 and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
