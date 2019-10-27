import random

class Particle:
    def __init__(self, dimension, function, funcType):
        #used to initialize starting velocity and position
        self.funcType = funcType
        #the location of the particle
        self.location = []
        #particle velocity
        self.velocity = []
        #personal best found, initialize as current position
        self.pBest = self.location
        #evaluation function
        self.function = function
        #personal best acceleration coefficient
        self.phi1 = 2.05
        #global best acceleration coefficient
        self.phi2 = 2.05
        #constriction factor
        self.phi = phi1 + phi2
        self.constrictionFactor = 0.7298

    def initPosition(self):
        print()

    def initVelovity(self):
        print()

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
        self.updateVelocity(pbAc,nbAc)
        for i in range(len(self.velocity)):
            self.position[i] += self.velocity[i]
        self.updatePersonalBest()

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

    #compute the velocity vector given personal best acceleration and
    #neighborhood best acceleration
    def updateVelocity(self,pbAc,nbAc):
        #constrict the new velocity and reset the current velocity
        for i in range(len(pbAc)):
            self.velocity[i] += pbAc[i] + nbAc[i]
            #constrict
            self.velocity[i] = self.velocity[i] * self.constrictionFactor

    def updatePersonalBest(self):
        currentFuncVal = self.getFunctionValue()
        pBestFuncVal = self.function(self.pBest)
        if currentFuncVal > pBestFuncVal:
            self.pBest = self.location
