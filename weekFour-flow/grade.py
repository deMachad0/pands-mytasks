# program that reads percentage marks
# and print out the grade 
# Author: Andre Machado

number = float(input("Enter the percentage: "))

if(number < 0 or number > 100):
    print("Enter a number between 0 and 100 please")
elif(number < 40):
    print("Fail")
elif(number < 50):
    print("Pass")
elif(number < 60):
    print("Merit 2")
elif(number < 70):
    print("Merit 1")
else:
    print("Distinction")
