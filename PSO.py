import sys
from Particle import Particle
from Function import Function
from Neighborhood import Neighborhood

class PSO:
    def __init__(self, topology, sizeSwarm, numIterations, funcType, dimension):
        self.topology = topology
        self.sizeSwarm = int(sizeSwarm)
        self.numIterations = int(numIterations)
        self.funcType = funcType
        self.function = Function(funcType,int(dimension))
        self.dimension = int(dimension)
        self.globalBestLocation = []
        self.globalBestValue = 10000000
        self.particles = []
        self.NH = Neighborhood(topology,int(dimension))

    #initialize a swarm of size self.sizeSwarm with randomly located particles
    def buildSwarm(self):
        #build sizeSwarm particles, by defualt they are initialized randomly
        for i in range(self.sizeSwarm):
            p = Particle(self.dimension,self.function,self.funcType)
            p.randomInit()
            self.particles += [p]
        #check for global best
        self.updateGlobalBest()

    #this method will individiually update partciles based on their personal
    #best location and their neighborhood best location
    def updateSwarm(self):
        for particle in self.particles:
            curIndex = self.particles.index(particle)
            nhBest = self.NH.getBestNeighbor(self.particles,particle.getFunctionValue(),particle.getLocation(),curIndex)
            particle.updateLocation(nhBest)

    #check to see if terminantion condition is met (found 0.0 function value)
    def minFound(self):
        if self.globalBestValue == 0.0:
            return True
        else:
            return False

    def printOutput(self):
        print("Min Value Found: ", self.globalBestValue)
        print("Min Location: ", self.globalBestLocation)

    #this method will look through all particles and find the global best
    def updateGlobalBest(self):
        for particle in self.particles:
            if particle.pBestValue() < self.globalBestValue:
                self.globalBestValue = particle.pBestValue()
                self.globalBestLocation = particle.pBest

    def run(self):
        self.buildSwarm()
        for i in range(self.numIterations):
            self.updateSwarm()
            self.updateGlobalBest()
            print("i: ", i)
            print("bestFound: ", self.globalBestValue)
            if self.minFound():
                break
        self.printOutput()

#Get paramater input from command line (topology, sizeSwarm, numIterations, function, dimension)
topology = sys.argv[1]
sizeSwarm = sys.argv[2]
numIterations = sys.argv[3]
function = sys.argv[4]
dimension = sys.argv[5]

#run the program
eA = PSO(topology,sizeSwarm,numIterations,function,dimension)
eA.run()
