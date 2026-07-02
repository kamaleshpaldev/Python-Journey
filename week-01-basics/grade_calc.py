# Program: Grade Calculator
# Concept: if else chain
# week: 1 - python basics

# asking user for input
marks = float(input("Enter your marks: "))

# calculating grade on basis of marks
if marks > 90:
    grade = "A"
elif marks > 75:
    grade = "B"
elif marks > 60 :
    grade = "C"
elif marks > 45 :
    grade = "D"
else:
    grade = "F"

#printing grade

print("You got Grade "+ grade)