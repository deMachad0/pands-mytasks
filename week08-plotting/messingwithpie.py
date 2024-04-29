#messing with pie

import numpy as np
import matplotlib.pylab as plt

fruits = np.array(["Orange", "Banana", "Apples"])
numbers = np.array([200, 500, 1000])

plt.pie(numbers, labels= fruits)
plt.show()