#the test-b.txt file exists ? 
#Answer : yes
#it will return the number of characters and lines written
#Author : Andre Machado

with open("test-b.txt", "w") as f:
    data = f.write("test b \n") # returns the number of chars
    print(data)

with open("test-b.txt", "w") as f2: # open the file again
    data = f2.write("another line \n")
    print(data)