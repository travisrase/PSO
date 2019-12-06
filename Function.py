import math

class Function:
    def __init__(self, funcType, dimension):
        #the tpye of function we are optimizing
        self.funcType = funcType

    #given a position vector of length dimension,
    #this function will return a function value,
    #from a function of type funcType at position
    def eval(self,location):
        try:
            if self.funcType == "roc":
                return self.evalRosenbrock(location)
            elif self.funcType == "ras":
                return self.evalRastrigin(location)
            else:
                return self.evalAckley(location)
        except:
            return 100000000

    #a function that given a vector in an n-dimensional space, will return
    #the Rosenrbock function value at that point.
    def evalRosenbrock(self,location):
        #Init return Val
        returnVal = 0
        # loop through dimension. for rosenbrock omit last dimension
        for i in range(len(location)- 1):
            xi = location[i]
            xi_plus_one = location[i+1]
            returnVal = 100.0 * pow(xi_plus_one - xi*xi, 2.0) * pow(xi - 1.0, 2.0)
        return returnVal

    #a function that given a vector in an n-dimensional space, will return
    #the Rastrigin function value at that point.
    def evalRastrigin(self,location):
        #Init return Val
        returnVal = 0
        #Loop through vector of dimensions
        for i in range(len(location)):
            xi = location[i]
            #Return val function for Rastrigin
            returnVal = xi*xi - 10.0 * math.cos(2 * math.pi * xi) + 10.0
        return returnVal

    #a function that given a vector in an n-dimensional space, will return
    #the Ackley function value at that point. 
    def evalAckley(self,location):
        firstSum = 0.0
        secondSum = 0.0
        for elem in location:
            firstSum += elem**2.0
            secondSum += math.cos(2.0*math.pi*elem)
        lengths = float(len(location))
        returnVal = -20.0*math.exp(-0.2*math.sqrt(firstSum/lengths)) - math.exp(secondSum/lengths) + 20 + math.e
        return (-20.0*math.exp(-0.2*math.sqrt(firstSum/lengths)) - math.exp(secondSum/lengths) + 20 + math.e)
