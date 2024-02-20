# Prompts the user to guess a number until
# the user gets the right on
# Author: Andre Machado

guess_number = int(input("Please guess the number: "))

right_number = 4

while guess_number !=  right_number:
    print("Wrong!")
    guess_number = (int(input("Try another number: "))) 

print("Well done! Yes the number was", right_number)
