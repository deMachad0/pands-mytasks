#messing with histograms

import numpy as np
import matplotlib.pyplot as plt

#make sure the graph will be the same 
np.random.seed(1)

normal_data = np.random.normal(size=10000)

#creating a histogram
plt.hist(normal_data)
plt.show()