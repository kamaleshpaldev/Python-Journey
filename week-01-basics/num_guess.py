# Program: NUmber guessing game 
# Concept: if-elif-else , variable
# week: 1 - python basics

# secret number
secNum= 37

#taking input form user
num = int(input("Whats your guess? : "))

#checking if guess is smaller , greater or correct

if num==secNum:
    print("yeahhh!!!! correct answer")
elif num<secNum:
    print("nope, the number is bigger then that , try agin !")
elif num>secNum:
    print("nope, the number is smaller then that , try agin !")
