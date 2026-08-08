
#       STUDENT GRADE CALCULATOR


print("       STUDENT GRADE CALCULATOR")


# Student details
name = input("Enter student name: ")

# Enter marks
english = float(input("Enter English marks: "))
maths = float(input("Enter Maths marks: "))
gen_ai = float(input("Enter Gen AI marks: "))
aptitude = float(input("Enter Aptitude marks: "))
back_end = float(input("Enter Back End marks: "))
front_end = float(input("Enter Front End marks: "))

# Calculate total
total = english + maths + gen_ai + aptitude + back_end + front_end

# Calculate percentage
percentage = total / 6

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Calculate result
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display result

print("             STUDENT RESULT")


print("Student Name :", name)

print("English      :", english)
print("Maths        :", maths)
print("Gen AI       :", gen_ai)
print("Aptitude     :", aptitude)
print("Back End     :", back_end)
print("Front End    :", front_end)

print("Total Marks  :", total, "/ 600")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
