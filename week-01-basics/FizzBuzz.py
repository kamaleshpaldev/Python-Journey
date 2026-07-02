# Program: FizzBuzz
# Concept: for loop , if-elif-else, modulo operator
# week: 1 - python basics

# What it does : print numbers from 1 to 50 
# but if number is multiple of three then it print Fizz,
# if number is multiple of five then it print Buzz
# if number is multiple of both 3 and 5 then it print FizzBuzz

for i in range(1,51):
    if i%3 == 0: 
        if i%5 == 0:
            print("Fizzbuzz") # when it is mulitiple of both 3 & 5 
        else:
            print("Fizz") # when it is mulitiple of 3

    elif i%5 == 0 :
        print("Buzz") # when it is mulitiple of 5

    else:
        print(i) # otherwise print number