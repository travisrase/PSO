import random

class Particle:
    def __init__(self, dimension, function):
        self.location = []
        #initialize random location
        for i in range (dimension):
            self.location += [random.random()]
        #personal best found, initialize as current position
        self.personalBestValue = self.location
        #evaluation function
        self.function = function
        #particle velocity
        self.velocity = 0


    #getter method for location
    def location(self):
        return self.location

    #setter method for location
    def setLocation(self,location):
        self.location = location

    #getter method for personal best
    def pBest(self):
        return self.personalBest

    #getter method for function value at current position
    def getFunctionValue(self):
        return self.function(self.location)
