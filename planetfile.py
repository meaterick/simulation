import numpy as np
from positionfile import position
from vectorfile import vector

class planet():
    def __init__(self):
        self.vector = vector()
        self.position = position()
        
    def gravity(self, planet):
        81 / ((self.position.x - planet.position.x)**2 +
        (self.position.x - planet.position.x)**2 +
        (self.position.x - planet.position.x)**2)
        