# Program: simmple calculator
# Concept: variable, input, output, if-else, arithmetic operations, type converison
# week: 1 - python basics

# taking inputs from user

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("press 1 to add")
print("press 2 to subtract")
print("press 3 to multiply")
print("press 4 to divide")
op = int(input(">"))

# Calculating answer

if op == 1:
    print(f"Answer is {num1+num2}")
elif op == 2:
    print(f"Answer is {num1-num2}")
elif op == 3:
    print(f"Answer is {num1*num2}")
elif op == 4:
    if num2==0: # handeling divide by zero error
        print("divide by zero is not possible")
    else:    
        print(f"Answer is {num1/num2}")
else:
    print("Choose from options only.")
