#a program that makes a list of salaries
#max salary = 80000, min salary = 20000, 10 random numbers
#Author: Andre Machado

import numpy as np

max_salary = 80000
min_salary = 20000
random_number = 10

#Modify the program so that the “random” salaries are the same each time the
#program is run, to make the program easier to test, is “seed” 
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, random_number)
#Modify the program, to make another array of numbers that has the salaries plus
#5000 
salaries_plus = salaries + 5000
#Modify the program so that it increases all the salaries by 5%
salaries_increase = salaries * 1.05

print(salaries)
print(salaries_plus)
print(salaries_increase)
