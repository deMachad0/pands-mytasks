# messing with files

# open a file a read it
FILENAME = "data.txt"


with open(FILENAME, 'r') as f:
    data = f.read()
    print(data)
    

#open a file ina different way
with open(FILENAME, 'rt') as f:
    # for to give a new line betweem the written lines
    for data in f:
        #strip() or end="" can be used to cut the extra lines
        #print(data, end="")
        #print(data[:-1])
        print(data.strip())
    

#open a file and create/writing 
with open("data2.txt", "w+") as f:
    f.write("how now \n")
    f.write("brown cow")
    # without .seek(0) the data is not going to be printed on the screen
    f.seek(0)
    data = f.read()
    print(data)

print("done")
