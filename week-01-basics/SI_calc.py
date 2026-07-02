# Program: simple interest calculator
# Concept: type conversion, f-strings, arithmetic
# week: 1 - python basics

#taking inputs from user
principle = float(input("enter principle amount: "))
interest = float(input("enter rate of interest: "))
time = int(input("enter time in years: "))

#finding simple interest
print(f"simple interest is {principle*interest*time/100}")