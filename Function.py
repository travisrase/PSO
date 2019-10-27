import math

class Function:
    def __init__(self, funcType, dimension):
        #the tpye of function we are optimizing
        self.funcType = functType

    #given a position vector of length dimension,
    #this function will return a function value,
    #from a function of type funcType at position
    def eval(self,location):
        if self.funcType == "roc":
            return self.evalRosenbrock(location)
        elif self.funcType == "ras":
            return self.evalRastrigin(location)
        else:
            return self.evalAckley(location)

    def evalRosenbrock(self,location):
        #Init return Val
        returnVal = 0
        # loop through dimension. for rosenbrock omit last dimension
        for i in range(len(location)- 1):
            xi = location[i]
            xi_plus_one = location[i+1]
            returnVal = 100.0 * pow(xi_plus_one - xi*xi, 2.0) * pow(xi - 1.0, 2.0)
        return returnVal

    def evalRastrigin(self,location):
        #Init return Val
        returnVal = 0
        #Loop through vector of dimensions
        for i in range(len(location)):
            xi = location[i]
            #Return val function for Rastrigin
            returnVal = xi*xi - 10.0 * math.cos(2 * math.pi * xi) + 10.0
        return returnVal

    def evalAckley(self,location):
        #Init sums
        firstSum = 0
        secondSum = 0
        for i in range(len(location)):
            xi = location[i]
            #Compute first and second sums
            firstSum += xi * xi
            secondSum += math.cos(2.0*math.pi*xi)
        #Return value function
        returnVal = -20.0 * math.exp(-0.2 * math.sqrt(firstSum / location.length())) - math.exp(secondSum / location.length()) + 20.0 + math.e
        return returnVal
