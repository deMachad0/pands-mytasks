#checking if an OS file exists
#Author : Andre Machado

import os.path

FILENAME = "count3.txt"
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))


if not os.path.isfile(FILENAME):
    print("File does not exist")
    writeNumber(0)