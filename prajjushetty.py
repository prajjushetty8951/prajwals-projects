from datetime import date

print("======================================")
print("     PERSONAL DETAILS CALCULATOR")
print("======================================")

# User details
name = input("Enter your name: ")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Date of birth
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Current date
today = date.today()

# Date of birth
dob = date(birth_year, birth_month, birth_day)

# Calculate age
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age = age - 1

# Calculate BMI
height_meter = height / 100
bmi = weight / (height_meter * height_meter)

# Display results
print("\n======================================")
print("             YOUR DETAILS")
print("======================================")

print("Name:", name)
print("Height:", height, "cm")
print("Weight:", weight, "kg")
print("Date of Birth:", dob.strftime("%d-%m-%Y"))
print("Age:", age, "years")
print("BMI:", round(bmi, 2))

print("======================================")
print("        Thank You!")
print("======================================")
