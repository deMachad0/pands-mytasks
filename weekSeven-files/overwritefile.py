#a program that overwrites a file
#Author: Andre Machado

FILENAME = "count.txt"
def write_number(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

write_number(3)
