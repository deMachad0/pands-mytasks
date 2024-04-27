#the test-a.txt file exists ? 
#Answer : no
#Author : Andre Machado

from os import remove


with open("test-a.txt") as f:
    data = f.read()
    print(data)

remove("test-a.txt")