import numpy as np
import math
from positionfile import position
from vectorfile import vector
from gravityfile import gravity

class planet():
    def __init__(self):
        self.vector = vector()
        self.position = position()
        self.gravity = gravity()
        self.mass = 0
        self.color = [0, 0, 0]
        
    def add(self, save, other1, other2):
        save.x = other1.x + other2.x
        save.y = other1.y + other2.y
        save.z = other1.z + other2.z
        
    def sub(self, save, other1, other2):
        save.x = other1.x - other2.x
        save.y = other1.y - other2.y
        save.z = other1.z - other2.z
        
    def set_mass(self, mass):
        self.mass = mass
        
    def set_color(self, color):
        self.color = color
        

    def distance(self, other):
        return(
            math.sqrt((self.position.x - other.position.x)**2 + (self.position.y - other.position.y)**2 + (self.position.z - other.position.z)**2)
        )

    def move(self, Gother):
        distance = self.distance(Gother)
        
        if distance == 0:
            return
        
        self.sub(self.gravity, Gother.position, self.position)
        self.vector.x = self.vector.x + (self.gravity.x / ((distance)**2) * self.mass * Gother.mass) / self.mass
        self.vector.y = self.vector.y + (self.gravity.y / ((distance)**2) * self.mass * Gother.mass) / self.mass
        self.vector.z = self.vector.z + (self.gravity.z / ((distance)**2) * self.mass * Gother.mass) / self.mass
        
        self.add(self.position, self.position, self.vector)
