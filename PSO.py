import sys

class PSO:
    def __init__(self, topology, sizeSwarm, numIterations, function, dimension):
        self.topology = topology
        self.sizeSwarm = sizeSwarm
        self.numIterations = numIterations
        self.function = function
        self.dimension = dimension

    def run(self):
        print()



#Get paramater input from command line (topology, sizeSwarm, numIterations, function, dimension)
topology = sys.argv[1]
sizeSwarm = sys.argv[2]
numIterations = sys.argv[3]
function = sys.argv[4]
dimension = sys.argv[5]

#run the program
eA = PSO(topology,sizeSwarm,numIterations,function,dimension)
eA.run()
