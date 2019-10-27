import random

class Particle:
    def __init__(self, dimension, function):
        self.location = []
        #initialize random location
        for i in range (dimension):
            self.location += [random.random()]
        #personal best found, initialize as current position
        self.pBest = self.location
        #evaluation function
        self.function = function
        #particle velocity
        self.velocity = 0
        #personal best acceleration coefficient
        self.phi1 = 2.05
        #global best acceleration coefficient
        self.phi2 = 2.05
        #constriction factor
        self.phi = phi1 + phi2
        self.constrictionFactor = 0.7298

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

    def updateLocation(self,nhBest):
        pbAc = self.pBestAcceleration()
        nbAc = self.nBestAcceleration(nhBest)
        velocity = self.computeVelocity(pbAc,nbAc)
        i = 0
        for vi in velocity:
            self.position[i] += vi
            i += 1

    #compute the acceleration due to personal best
    def pBestAcceleration(self):
        pbAc = []
        i = 0
        #compute acceleration as difference between current location and personal
        #best location in self.dimensions dimenions
        for pbi in self.pBest:
            iAc = pbi - self.location[i]
            iAc = iAc*self.phi1*random.random()
            pbAc += [iAc]
            i += 1
        return pbAc

    #compute the acceleration due to neighborhood best
    def nBestAcceleration(self,nhBest):
        nbAc = []
        i = 0
        #compute acceleration as difference between current location and neighborhood
        #best location in self.dimensions dimenions
        for nbi in nhBest:
            iAc = nbi - self.location[i]
            iAc = iAc*self.phi2*random.random()
            pbAc += [iAc]
            i += 1
        return nbAc

    def computeVelocity(self,pbAc,nbAc):
        #constrict the new velocity and reset the current velocity
        velocity = []
        for i in range(len(pbAc)):
            v = pbAc[i] + nbAc[i]
            #constrict
            v = v * self.constrictionFactor
            velocity += [v]
        return velocity
