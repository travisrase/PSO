import random

class Neighborhood:
    def __init__(self, neighborhoodType, dimension):
        self.neighborhoodType = NeighborhoodType
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
                curLocation = particles[i].location()
                if curVal > glBest:
                    glBest = curVal
                    glBestLocation = curLocation
            return glBestLocation
        elif self.NeighborhoodType == 'ri':
            asdf
        elif self.NeighborhoodType == 'vn':
            asdf
        elif self.NeighborhoodType == 'ra':
            neighborhoodSize = random.randInt(0, len(particles))
            loBest = 0
            loBestLocation = []
            for i in range(len(particles)):

        return [0]
