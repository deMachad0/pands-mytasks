# user inputs 2 numbers and the program multiples them
# Author: Andre Machado

'''
number1 = False
while(number1 == False):
  try:
    number1 = int(input("Enter a Number: "))
  except ValueError:
    print("that was not a number, try again: ", end="") 
    

number2 = False
while(number2 == False):
  try: 
    number2 = int(input("and another number: "))
  except ValueError:
    print("that was not a number, try again: ", end="")

answer = number1 * number2

print(f"Answer is {answer}") 

'''

''' end="" to cut space'''


# using function (def) for a better code

def readNum(message = "Enter a number: "):
  number = False
  while(not number):
    try:
      number = int(input(message))
    except ValueError:
      print("that was not a number, try again: ", end="")
  return number

number1 = readNum()
number2 = readNum("Enter number2: ")

answer = number1 * number2

print(f"Answer is : {answer}")