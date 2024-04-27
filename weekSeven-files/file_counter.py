# a program that counts how many times it was run
# usind a function def 
# Author: Andre Machado

FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
num = read_number()
print(num)