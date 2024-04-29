#messing with matplot

import numpy as np
import matplotlib.pyplot as plt

#creating an array betweem 1 to 100
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#creating a graph using matplot
plt.plot(xpoints, ypoints)
#defining legend name and color
plt.plot(xpoints, xpoints, label="straight", color="blue")
#showing legend in the graph
plt.legend()

#creating random points
random_points = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, random_points, label="random", color="green")
plt.legend()

#saving the graph as png 
plt.savefig("lecture1.png")
plt.show()