# Prompts the user to guess a number until
# the user gets the right on
# Author: Andre Machado


guess_number = int(input("Please guess the number: "))

right_number = 30

while guess_number !=  right_number:
    if guess_number < 30:
        print("too low")
    else:
        print("too high")
    guess_number = (int(input("Try another number: "))) 

print("Well done! Yes the number was", right_number)
