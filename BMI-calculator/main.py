#Day 2
print("Welcome to BMI calculator")

weight = float(input("Enter your body weight in Kgs: "))
height = float(input("Enter your height in meters: "))

bmi = weight/(height**2)
print("your BMI is "+str(int(bmi)))
