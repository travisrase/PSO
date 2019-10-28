import random

class Neighborhood:
    def __init__(self, neighborhoodType, dimension):
        self.neighborhoodType = neighborhoodType
        self.dimension = dimension

    #given all the particles in the swarm and the location
    #of a particle, it will return the location of the best
    #particle in its neighborhood.
    def getBestNeighbor(self,particles,position):
        if self.NeighborhoodType == 'gl':
            glBest = 0
            glBestLocation = []
            for i in range(len(particles)):
                curVal = particles[i].getFunctionValue()
                curLocation = particles[i].getLocation()
                if curVal > glBest:
                    glBest = curVal
                    glBestLocation = curLocation
            return glBestLocation
        elif self.NeighborhoodType == 'ri':
            loBest = 0
            loBestLocation = []


            return loBestLocation
        elif self.NeighborhoodType == 'vn':
            loBest = 0
            loBestLocation = []

            return loBestLocation
        elif self.NeighborhoodType == 'ra':
            ### NEED probabalistic neighborhood of previous type
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
            return loBestLocation

        return [0]
