class Particle:
    def __init__(self, dimension, function):
        self.location = [0]*dimension
        self.functionValue = function(self.location)
        self.velocity = 0
        self.personalBest = [0]*dimension
