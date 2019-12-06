import random
import numpy as np

class Neighborhood:
    def __init__(self, neighborhoodType, dimension):
        self.neighborhoodType = neighborhoodType
        self.dimension = dimension
        #self.previousRAneigh = None
        #self.previousVNneigh = None
        self.neighbors = None


    """This helper method initializes a neighborhood for a given problem type."""
    def initNeighbors(self, particles, curIndex):
        if self.neighborhoodType == 'gl':
            self.neighbors = particles
        elif self.neighborhoodType == 'ri':
            self.neighbors = self.riBestNeighbor(particles, curIndex)
        elif self.neighborhoodType == 'vn':
            self.neighbors = self.vnNeighbors(particles, curIndex)
        elif self.neighborhoodType == 'ra':
            self.neighbors = self.raNeighbors(particles, curIndex)


    """Given all the particles in the swarm and the location
    of a particle, it will return the location of the best
    particle in its neighborhood."""
    def getBestNeighbor(self, particles, curScore, position, curIndex):
        if self.neighbors == None:
            self.initNeighbors(particles, curIndex)
        else:
            if self.neighborhoodType== 'gl':
                return self.getBestLocation(self.neighbors, curScore, position)
            elif self.neighborhoodType== 'ri':
                #neighbors = riBestNeighbor(particles, curScore, position, curIndex)
                return self.getBestLocation(self.neighbors, curScore, position)
            elif self.neighborhoodType== 'vn':
                #locationNeighborhood = self.vnBestNeighbor(particles, curScore, position, curIndex, self.previousVNneigh)
                #self.previousVNneigh = locationNeighborhood[1] locationNeighborhood[0]
                return self.getBestLocation(self.neighbors, curScore, position)
            elif self.neighborhoodType== 'ra':
                #locationNeighborhood = self.raBestNeighbor(particles, curScore, position, self.previousRAneigh)
                #self.previousRAneigh = locationNeighborhood[1]locationNeighborhood[0]
                self.raNeighbors()
                return self.getBestLocation(self.neighbors, curScore, position)
            else:
                return position

    """Helper method that returns the best neighbor when given a neighborhood."""
    def getBestLocation(self, neighborhood, curScore, position):
        loBest = curScore
        loBestLocation = position
        for neighbor in self.neighbors:
            neighborVal = neighbor.getFunctionValue()
            if neighborVal < loBest:
                loBest = neighborVal
                loBestLocation = neighbor.getLocation()
        return loBestLocation

    #Helper method used to find the best neighbor in global swarm topology
    #Uses the list of particles and the current particles position to determine
    #the best location found so far in the swarm.
    # def glBestNeighbor(self, particles,position,):
    #     glBest = 100000000
    #     glBestLocation = position
    #     for particle in particles:
    #         if particle.getFunctionValue() < glBest:
    #             glBest = particle.getFunctionValue()
    #             glBestLocation = particle.getLocation()
    #     return glBestLocation


    """Helper method used to create the ring swarm neighborhood topology.
    Uses the list of particles, the evaluation of the current particle, the
    current particles position, and the current particle's index to
    create the neighborhood."""
    def riNeighbors(self, particles, curIndex):
        #loBest = curScore
        #loBestLocation = position
        #neighbors = []
        if curIndex == (len(particles) - 1):
            self.neighbors.append(particles[curIndex - 1])
            self.neighbors.append(particles[0])
        elif curIndex <= (len(particles) - 2):
            self.neighbors.append(particles[curIndex - 1])
            self.neighbors.append(particles[curIndex + 1])
        #return self.neighbors
        # for neighbor in neighbors:
        #     if neighbor.getFunctionValue() < loBest:
        #         loBest = neighbor.getFunctionValue()
        #         loBestLocation = neighbor.getLocation()
        # return loBestLocation


    """Helper methods used to find the neighborhood in von Neumann swarm topology."""
    def vnNeighborsHelper(self, numPart):
        width = 0
        height = 0
        if numPart == 16:
            width = 4
            height = 4
        elif numPart == 30:
            width = 5
            height = 6
        else:
            width = 7
            height = 7
        topology = [[None] * width] * height
        i = 0
        while i < len(particles):
            #modulo population of the topology
            rollover = 0
            while rollover < width:
                horizontal = i % width
                topology[horizontal][rollover] = particles[i]
                rollover = rollover + 1
                i = i + 1
        return (topology, width, height)

    def vnNeighbors(self, particles, curIndex):
        #neighborhood = prevNeighbors
        if self.neighbors == None:
            neighborhood = self.vnNeighborsHelper(len(particles))
        #loBest = curScore
        #loBestLocation = position
        #shape = self.vnBestNeighborHelper(particles)
        topology = neighborhood[0]
        width = curIndex % neighborhood[1]
        height = curIndex // neighborhood[2]
        #Add left & above neighbors to neighbors list
        neighbors = []
        self.neighbors.append(topology[width - 1][height])
        self.neighbors.append(topology[width][height - 1])
        #get neighbor to the right
        if width + 1 <= (shape[1] - 2):
            self.neighbors.append(topology[width + 1][height])
        else:
            self.neighbors.append(topology[0][height])
        #get neighbor below
        if height + 1 <= shape[2] - 2:
            self.neighbors.append(topology[width][height + 1])
        else:
            self.neighbors.append(topology[width][0])
        #return self.neighbors
        # for neighbor in neighbors:
        #     if neighbor.getFunctionValue() < loBest:
        #         loBest = neighbor.getFunctionValue()
        #         loBestLocation = neighbor.getLocation()
        # return (loBestLocation, shape)


    """Helper method used to find the best neighbor in random swarm topology
    Uses the list of particles, the evaluation of the current particle, the
    current particle's position, and the list of its previous neighbors to
    find the best location found so far in the swarm."""
    def raNeighbors(self, particles, curIndex):#, particles, curScore, position, prevNeighbors):
        if random.random() > 0.8 OR self.neighbors == None:
            # loBest = curScore
            # loBestLocation = position
            # for i in range(len(prevNeighbors) - 1):
            #     curPart = particles[prevNeighbors[i]]
            #     curLocation = curPart.getLocation()
            #     curVal = curPart.getFunctionValue()
            #     if curVal < loBest:
            #         loBest = curVal
            #         loBestLocation = curLocation
            # return (loBestLocation, prevNeighbors)
            self.neighbors = None
            neighborhoodSize = 5
            #loBest = curScore
            #loBestLocation = position
            neighborhood = {}
            neighbors = []
            while len(neighborhood) < neighborhoodSize:
                #create a list of all indexes other than the current index
                range = range(1, curindex) + range(curIndex + 1, len(particles))
                #neighborhood.append(random.randint(0, len(particles)))
                neighborhood.append(random.choice(range))
            neighborhood = list(neighborhood)
            for i in range(len(neighborhood) - 1):
                self.neighbors.append(particles[neighborhood[i]])
            #return neighbors



            #neighbors = sorted(neighborhood)
            # for i in range(len(neighbors) - 1):
            #     curPart = particles[neighbors[i]]
            #     if curPart.getFunctionValue() < loBest:
            #         loBest = curPart.getFunctionValue()
            #         loBestLocation = curPart.getLocation()
            # return (loBestLocation, neighbors)
