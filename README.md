# PSO
Particle Swarm Optimizer
The function implements a Particle Swarm Optimizer, along with four Neighborhood Topologies: Global, Ring, Random, and 
von Nuemann. Additionally three n-dimesnional benchmark functions have also been programed that allow you to run 
the optimizer on a search for a global minimum: Rosenbrock, Ackley, and Rastrigin. 

The program will output the minimum function value found, the location of the minimum function value found, and the number of iterations needed to reach that function value. 

Note: if a 0.0 value is not found, then it will run until it reaches the max number of iterations paramater. 

When running this fucntion you can vary 5 paramaters: 
1. The Neighborhood Topology (gl: Global, ri: Ring, ra: Random, vn: von Nuemann)
2. The Size of the Swarm. This can be any nonzero positive integer. Good values to use range from (5-100)
3. The number of iterations
4. The test function (rok: Rosenbrock, ack: Ackley, ras: Rastrigin, default: ack)
5. The dimension of the function space

The paramaters are given in this order. 

For example call 

$ Python3 PSO.py ra 50 100 ras 5

for a random topology, with a swarm of size 50, and 100 max iterations, to maximize the Rastrigin function in 5 dimensions. Calling this function produced the following output: 

Minimum Value Found:  2.4935786768764956e-09
Minimum Value Location:  [11931770.343513707, -6036736207.357395, 55592492.17690934, 14575667.905881414, 0.001127994006203073]
Number of Iterations:  100
