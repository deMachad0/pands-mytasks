# messing with OS module

#learning how to check if some file exists and print out it
import os

FILENAME = "messingwithfiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, 'r') as f:
        for line in f:
            print(line, end="")
else:
    print(FILENAME, "does not exist")



# how to remove an existed file
os.remove("data2.txt")