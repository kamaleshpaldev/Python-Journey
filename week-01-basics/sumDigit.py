# Program: Sum of Digit
# Concept: while loop ' modulo operator
# week: 1 - python basics

#asking for input
num = int(input("enter the number: "))

sum = 0

while num: # when num will become 0 it will act as false
    sum += num%10 # adding last digit to sum
    num//=10 # removing last digit

print(f'Sum of digits is {sum}')
    