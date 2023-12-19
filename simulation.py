import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from planetfile import planet

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

earth = planet()
earth.position.set(0, 0, 0)
earth.vector.set(0, 0, 0)
earth.set_mass(8.1)

moon = planet()
moon.position.set(0, 10, 0)
moon.vector.set(-2.55, 0, 0)
moon.set_mass(0.1)

while True:
    ax.clear()
    
    moon.move(earth)
    earth.move(moon)
    
    for theta1 in np.arange(0, 2*math.pi, math.pi/ 4):
        for theta2 in np.arange(0, math.pi, math.pi/4):
            x = math.cos(theta1) * math.sin(theta2)
            y = math.sin(theta1) * math.sin(theta2)
            z = math.cos(theta2)
            
            distance2 = math.sqrt((moon.position.x - earth.position.x)**2 + (moon.position.y - earth.position.y)**2 + (moon.position.z - earth.position.z)**2)
            distance1 = math.sqrt((x - moon.position.x)**2 + (y - moon.position.y)**2 + (z - moon.position.z)**2)
            if (distance2+0.7 < distance1):
                ax.scatter(x, y, z, c='r', alpha=distance1/14)
            elif (distance2-0.7 > distance1):
                ax.scatter(x, y, z, c='r', alpha=distance1/14)
            else:
                ax.scatter(x, y, z, c='b')
    
    ax.plot(*moon.position.loc(), marker="o", markersize=4, color='g')
    
    ax.plot(*earth.position.loc(), marker="o", markersize=20, color='b', alpha=0)
    
    ax.plot(*(-15, -15, -15), marker="o", markersize=1, color='r')
    ax.plot(*(15, 15, 15), marker="o", markersize=1, color='r')
    
    plt.pause(0.001)


plt.show()
