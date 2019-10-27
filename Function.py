import math

class Function:
    def __init__(self, vector):
        # A vrecotr of dimensions that are used to compute the return values 
        self.vector = vector

    #given a position vector of length dimension,
    #this function will return a function value,
    #from a function of type funcType at position
   
    def evalRosenbrock(self):
        #Init return Val
        returnVal = 0
        # loop through dimension. for rosenbrock omit last dimension
        for i in range(self.vector.length()- 1):
            xi = self.vector[i]
            xi_plus_one = self.vector[i+1]
            returnVal = 100.0 * pow(xi_plus_one - xi*xi, 2.0) * pow(xi - 1.0, 2.0)
        return returnVal

    def evalRastrigin(self):
        #Init return Val
        returnVal = 0
        #Loop through vector of dimensions 
        for i in range(self.vector.length()):
            xi = self.vector[i]
            #Return val function for Rastrigin
            returnVal = xi*xi - 10.0 * math.cos(2 * math.pi * xi) + 10.0
        return returnVal

    def evalAckley(self):
        #Init sums 
        firstSum = 0
        secondSum = 0
        for i in range(self.vector.length):
            xi = self.vector[i]
            #Compute first and second sums
            firstSum += xi * xi
            secondSum += math.cos(2.0*math.pi*xi)
        #Return value function
        return -20.0 * math.exp(-0.2 * math.sqrt(firstSum / self.vector.length())) - math.exp(secondSum / self.vector.length()) + 20.0 + math.e
