class vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def add(self, vector):
        return(
            self.x + vector.x,
            self.y + vector.y,
            self.z + vector.z
        )
    def sub(self, vector):
        return(
            self.x - vector.x,
            self.y - vector.y,
            self.z - vector.z
        )
        
        
    # def __dot__(self, vector):
    #     return(
    #         self.x 
    #     )
        
        