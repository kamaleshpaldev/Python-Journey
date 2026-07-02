# Program: Mulitplication table
# Concept: for loop , f-string
# week: 1 - python basics

# taking input from user
num = int(input("Enter number for multiplication table: "))

# printing table
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")