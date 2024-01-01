import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from planetfile import planet
import random

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

blackhole = planet()
p1 = planet()
p2 = planet()
p3 = planet()
p4 = planet()
p5 = planet()
p6 = planet()
p7 = planet()
p8 = planet()
p9 = planet()
p10 = planet()


planetlist = [blackhole, p1, p2, p3, p4, p5, p6, p7, p8 ,p9 ,p10]

for i in planetlist:
    if (i != blackhole):
        i.position.set(random.uniform(-150, 150), random.uniform(-150, 150), random.uniform(-150, 150))
        i.vector.set(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        i.set_mass(random.uniform(0.01, 4))
        
        colors = np.random.rand(3)
        i.set_color(colors)
    else:
        blackhole.position.set(0, 0, 0)
        blackhole.vector.set(0, 0, 0)
        blackhole.set_mass(7)
    
def regen(_planet):
    _planet.position.set(random.uniform(-150, 150), random.uniform(-150, 150), random.uniform(-150, 150))
    _planet.vector.set(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
    _planet.set_mass(random.uniform(0.01, 4))
    

# earth = planet()
# earth.position.set(0, 0, 0)
# earth.vector.set(0, 0, 0)
# earth.set_mass(8.1)

# moon = planet()
# moon.position.set(0, 10, 0)
# moon.vector.set(-2.55, 0, 0)
# moon.set_mass(0.1)

frame_rate = 0.01  # Time between frames in seconds
path_length = int(0.1 / frame_rate)  # Store positions for 1 second
for planet in planetlist:
    planet.path = [planet.position.loc() for _ in range(path_length)]

while True:
    ax.clear()
    
    for planet1 in planetlist:
        if (abs(planet1.position.x) > 300 or abs(planet1.position.y) > 300 or abs(planet1.position.z) > 300):
            regen(planet1)
        
        for planet2 in planetlist:
            if (planet1 != blackhole):
                if (planet1 != planet2):
                    planet1.move(planet2)

    for planet in planetlist:
        if (planet == blackhole):
            ax.plot(*planet.position.loc(), marker="o", markersize=15, color='black')
        else:
            ax.plot(*planet.position.loc(), marker="o", markersize=4, color=planet.color)
            
        planet.path.pop(0)
        planet.path.append(planet.position.loc())

        path_array = np.array(planet.path).T
        ax.plot(path_array[0], path_array[1], path_array[2], color='gray', alpha=0.5)
        
    # for i in range(1, len(planetlist)):
    #     ax.plot([planetlist[i - 1].position.x, planetlist[i].position.x],
    #             [planetlist[i - 1].position.y, planetlist[i].position.y],
    #             [planetlist[i - 1].position.z, planetlist[i].position.z],
    #             color='gray', linestyle='dashed', linewidth=1)
        
    # moon.move(earth)
    # earth.move(moon)
    
    # for theta1 in np.arange(0, 2*math.pi, math.pi/ 4):
    #     for theta2 in np.arange(0, math.pi, math.pi/4):
    #         x = math.cos(theta1) * math.sin(theta2)
    #         y = math.sin(theta1) * math.sin(theta2)
    #         z = math.cos(theta2)
            
    #         distance2 = math.sqrt((moon.position.x - earth.position.x)**2 + (moon.position.y - earth.position.y)**2 + (moon.position.z - earth.position.z)**2)
    #         distance1 = math.sqrt((x - moon.position.x)**2 + (y - moon.position.y)**2 + (z - moon.position.z)**2)
    #         if (distance2+0.7 < distance1):
    #             ax.scatter(x, y, z, c='r', alpha=distance1/14)
    #         elif (distance2-0.7 > distance1):
    #             ax.scatter(x, y, z, c='r', alpha=distance1/14)
    #         else:
    #             ax.scatter(x, y, z, c='b')
    
    # ax.plot(*moon.position.loc(), marker="o", markersize=4, color='g')
    
    # ax.plot(*earth.position.loc(), marker="o", markersize=20, color='b', alpha=1)
    
    ax.set_xlim([-200, 200])
    ax.set_ylim([-200, 200])
    ax.set_zlim([-200, 200])
    
    ax.plot(*(-300, -300, -300), marker="o", markersize=0, color='r')
    ax.plot(*(300, 300, 300), marker="o", markersize=0, color='r')
    
    plt.pause(0.001)


plt.show()
