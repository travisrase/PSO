class Particle:
    def __init__(self, dimension, function):
        self.location = [0]*dimension
        self.functionValue = function(self.location)
        self.velocity = 0
        self.personalBest = [0]*dimension

    #getter method
    def getLocation(self):
        return self.location

    #setter method for location
    def setLocation(self,location):
        self.location = location
        
