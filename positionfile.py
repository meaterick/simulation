class position():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def loc(self):
        return(
            self.x,
            self.y,
            self.z
        )