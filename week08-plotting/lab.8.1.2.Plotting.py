#Write a program that plots the function y = x2.
#Author: Andre Machado

import numpy as np
import matplotlib.pylab as plt

ypoints = np.array(range(1,101))
xpoints = ypoints * ypoints

plt.plot(xpoints, ypoints)
plt.show()