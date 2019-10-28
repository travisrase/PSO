import random

class Neighborhood:
    def __init__(self, neighborhoodType, dimension):
        self.neighborhoodType = neighborhoodType
        self.dimension = dimension

    #given all the particles in the swarm and the location
    #of a particle, it will return the location of the best
    #particle in its neighborhood.
    def getBestNeighbor(self,particles, curScore, position):

        if self.NeighborhoodType == 'gl':
            return self.glBestNeighbor(particles, curScore, position)
        elif self.NeighborhoodType == 'ri':
            return self.riBestNeighbor(particles, curScore, position)
        elif self.NeighborhoodType == 'vn':
            return self.vnBestNeighbor(particles, curScore, position)
        elif self.NeighborhoodType == 'ra':
            ## figure out prevNeighbors syntax in the initial case
            locationNeighborhood = self.raBestNeighbor(particles, curScore, position, prevNeighbors)
            prevNeighbors = locationNeighborhood[1]
            return locationNeighborhood[0]
        else:
            return position
          
    def glBestNeighbor(self, particles, curScore, position):
        glBest = curScore
        glBestLocation = []
        for i in range(len(particles)):
            curVal = particles[i].getFunctionValue()
            curLocation = particles[i].getLocation()
            if curVal > glBest:
                glBest = curVal
                glBestLocation = curLocation
        return glBestLocation
      
    def riBestNeighbor(self, particles, curScore, position):
        loBest = 0
        loBestLocation = []
        ### Maybe select two particles in the same dimension?

        return loBestLocation

    def vnBestNeighbor(self, particles, curScore, position):
        loBest = curScore
        loBestLocation = position
        ### similar problem as above
        return loBestLocation

    def raBestNeighbor(self, particles, curScore, position, prevNeighbors):
        if random.random() <= 0.2 && len(prevNeighbors) != 0:
            loBest = curScore
            loBestLocation = position
            for i in range(len(prevNeighbors)):
                curPart = particles[prevNeighbors[i]]
                curLocation = curPart.getLocation()
                if curVal > loBest:
                    loBest = curVal
                    loBestLocation = curLocation
            return (loBestLocation, prevNeighbors)
        else:
            neighborhoodSize = random.randInt(0, len(particles))
            loBest = 0
            loBestLocation = []
            neighborhood = set()
            while len(neighborhood) < neighborhoodSize:
                neighborhood.append(random.randInt(0, len(particles)))
            neighbors = sorted(neighborhood)
            for i in range(len(neighbors)):
                curPart = particles[neighbors[i]]
                if
            return (loBestLocation, neighbors)

