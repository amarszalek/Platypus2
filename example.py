from platypus import NSGAIII, DTLZ2
import time
# define the problem definition
problem = DTLZ2(3)

# instantiate the optimization algorithm
algorithm = NSGAIII(problem, divisions_outer=12)

# optimize the problem using 10,000 function evaluations
st = time.process_time()
algorithm.run(10000)
print(time.process_time() - st)

print(algorithm.nfe)
print(algorithm.iterate_num)

# plot the results using matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter([s.objectives[0] for s in algorithm.result],
           [s.objectives[1] for s in algorithm.result],
           [s.objectives[2] for s in algorithm.result])
plt.show()
