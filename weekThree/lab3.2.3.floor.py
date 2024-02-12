# floors a number
# Author: Andre Queiroz


import math


number = float(input("Enter a number: "))
result = math.floor(abs(number))

print('{} floored is {}'.format(abs(number), result))