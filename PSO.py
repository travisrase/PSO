import sys
from Particle import Particle
from Function import Function

class PSO:
    def __init__(self, topology, sizeSwarm, numIterations, function, dimension):
        self.topology = topology
        self.sizeSwarm = sizeSwarm
        self.numIterations = numIterations
        self.function = Function(function)
        self.dimension = dimension
        self.globalBestLocation = []
        self.globalBestValue = 0
        self.particles = []

    def buildSwarm(self):
        for i in range(self.sizeSwarm):
            p = Particle(self.dimension,)
            self.particles += [p]

    def run(self):
        self.buildSwarm()



#Get paramater input from command line (topology, sizeSwarm, numIterations, function, dimension)
topology = sys.argv[1]
sizeSwarm = sys.argv[2]
numIterations = sys.argv[3]
function = sys.argv[4]
dimension = sys.argv[5]

#run the program
eA = PSO(topology,sizeSwarm,numIterations,function,dimension)
eA.run()
