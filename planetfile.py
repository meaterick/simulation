import numpy as np
from positionfile import position
from vectorfile import vector

class planet():
    def __init__(self):
        self.vector = vector()
        self.position = position()
        
    def move(self):
        self.position.loc += self.vector.value
        return(
            self.position.loc
        )
        
