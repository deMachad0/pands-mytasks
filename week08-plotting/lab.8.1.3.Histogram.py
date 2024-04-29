#Write a program that plots a histogram of the salaries 
#Author: Andre Machado


import numpy as np
import matplotlib.pyplot as plt

max_salary = 80000
min_salary = 20000
random_number = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, random_number)
plt.hist(salaries)
#plt.show()
#Write a program that makes a list called ages that has, the same number random
#values as salaries, (range:21 to 65) . Make scatter plot of this data.
ages = np.random.randint(low=21, high=65, size =random_number)
plt.scatter(ages, salaries)
#plt.show()

#Add a line to this plot that shows y= x2 in a different colour
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color="r")
#plt.show()

#Add a legend, title and axis labels to this plot
plt.title("Random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show()

#save this to a file called "prettier-plot.png"
plt.savefig("prettier-plt.png")