# messing with numpy

import numpy as np

list_of_numbers = [1,2,3,4,"asass"]
list_of_numbers = list_of_numbers + [3]
print(list_of_numbers)

#Numpy arrays can only receive one variable type (string,int or..)
number = np.array([1,2,3,4])
#math operation with the array
number = number + 3
number = number + [1,2,3,4]

print(number)

#generate 30 random numbers bewteen 100-200
rando = np.random.randint(100,200,30)
print(rando)

normalrando = np.random.normal(size=100)
print(normalrando)
normalrando1 = np.random.normal(loc= 50, scale= 20, size= 100)
print(normalrando1)