# a program that shows if input provided is even or odd
# Author: Andre Machado

number = int(input("Enter a Number: "))

if (number % 2) == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")