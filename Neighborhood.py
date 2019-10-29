import random
import numpy

class Neighborhood:
    def __init__(self, neighborhoodType, dimension):
        self.neighborhoodType= neighborhoodType
        self.dimension = dimension
        self.previousVNneigh = None

    #given all the particles in the swarm, the evaluation of the current
    #particle, the location of the current particle, and the index of the
    #current particle, it will return the location of the best
    #particle in its neighborhood.
    def getBestNeighbor(self, particles, curScore, position, curIndex):
        if self.neighborhoodType== 'gl':
            return self.glBestNeighbor(particles, curScore, position)
        elif self.neighborhoodType== 'ri':
            return self.riBestNeighbor(particles, curScore, position, curIndex)
        elif self.neighborhoodType== 'vn':
            return self.vnBestNeighbor(particles, curScore, position)
        elif self.neighborhoodType== 'ra':
            locationNeighborhood = self.raBestNeighbor(particles, curScore, position, self.previousVNneigh)
            self.previousVNneigh = locationNeighborhood[1]
            return locationNeighborhood[0]
        else:
            return position

    #Helper method used for global neighborhood topology
    def glBestNeighbor(self, particles,curScore, position):
        glBest = curScore
        glBestLocation = position
        for particle in particles:
            if particle.getFunctionValue() < glBest:
                glBest = particle.getFunctionValue()
                glBestLocation = particle.getLocation()
        return glBestLocation

    #Helper method used for ring neighborhood topology
    def riBestNeighbor(self, particles, curScore, position, curIndex):
        loBest = curScore
        loBestLocation = position
        neighbors = []
        if curIndex == (len(particles) - 1):
            neighbors.append(particles[curIndex - 1])
            neighbors.append(particles[0])
        elif curIndex <= (len(particles) - 2):
            neighbors.append(particles[curIndex - 1])
            neighbors.append(particles[curIndex + 1])
        for neighbor in neighbors:
            if neighbor.getFunctionValue() < loBest:
                loBest = neighbor.getFunctionValue()
                loBestLocation = neighbor.getLocation()
        return loBestLocation

    #Helper method used for von Neumann neighborhood topology
    def vnBestNeighbor(self, particles, curScore, position):
        loBest = curScore
        loBestLocation = position
        neighbors = []
        for particle in particles:
            if sum(numpy.subtract(position, particle.getLocation())) < self.dimension:
                neighbors += [particle]
        for neighbor in neighbors:
            if neighbor.getFunctionValue() < loBest:
                loBest = neighbor.getFunctionValue()
                loBestLocation = neighbor.getLocation()
        return loBestLocation

    #Helper method used for random neighborhood topology
    def raBestNeighbor(self, particles, curScore, position, prevNeighbors):
        if random.random() <= 0.2 and  prevNeighbors != None:
            loBest = curScore
            loBestLocation = position
            for i in range(len(prevNeighbors) - 1):
                curPart = particles[prevNeighbors[i]]
                curLocation = curPart.getLocation()
                curVal = curPart.getFunctionValue()
                if curVal < loBest:
                    loBest = curVal
                    loBestLocation = curLocation
            return (loBestLocation, prevNeighbors)
        else:
            neighborhoodSize = random.randint(0, len(particles))
            loBest = curScore
            loBestLocation = position
            neighborhood = []
            while len(neighborhood) < neighborhoodSize:
                neighborhood.append(random.randint(0, len(particles)))
            neighborhood = set(neighborhood)
            neighbors = sorted(neighborhood)
            for i in range(len(neighbors) - 1):
                curPart = particles[neighbors[i]]
                if curPart.getFunctionValue() < loBest:
                    loBest = curPart.getFunctionValue()
                    loBestLocation = curPart.getLocation()
            return (loBestLocation, neighbors)
