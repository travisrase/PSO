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
        self.globalBestValue = 0
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
            nhBest = self.NH.getBestNeighbor(self.particles,particle.location())
            particle.updateLocation(nhBest)

    #this method will look through all particles and find the global best
    def updateGlobalBest(self):
        for particle in self.particles:
            if particle.pBestValue() > self.globalBestValue:
                self.globalBestValue = particle.pBestValue()
                self.globalBestLocation = particle.getLocation()

    def run(self):
        self.buildSwarm()
        print("numParticles: ", len(self.particles))
        print("global best location : ", self.globalBestLocation)
        print("global best value: ", self.globalBestValue)
        for i in range(self.numIterations):
            self.updateSwarm()


#Get paramater input from command line (topology, sizeSwarm, numIterations, function, dimension)
topology = sys.argv[1]
sizeSwarm = sys.argv[2]
numIterations = sys.argv[3]
function = sys.argv[4]
dimension = sys.argv[5]

#run the program
eA = PSO(topology,sizeSwarm,numIterations,function,dimension)
eA.run()
