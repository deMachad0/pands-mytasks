#a program that counts how many times
#the program has been run
#Author: Andre Machado

FILENAME = "count2.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def write_number(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

num = read_number()
num += 1
print(f"this program has run {num} times")
write_number(num)