import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from planetfile import planet

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

earth = planet()
earth.position.set(0, 0, 0)

moon = planet()
moon.position.set(0, 167, 0)

for i in np.arange(-100, 100, 1):
    ax.plot(*moon.position.loc(), marker="o", markersize=4, color='g')
    
    ax.plot(*earth.position.loc(), marker="o", markersize=20, color='b')
    
    ax.plot(*(-100, -100, -100), marker="o", markersize=1, color='r')
    ax.plot(*(100, 100, 100), marker="o", markersize=1, color='r')
    plt.pause(0.001)
    ax.clear()


plt.show()