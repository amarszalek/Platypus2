from platypus import IMGAMO, DTLZ2
from platypus import MutateIMGAMOHiper, MutateIMGAMOUniform, MutateIMGAMOBound, MutateIMGAMOGaussian
import time
# define the problem definition
problem = DTLZ2(3)

# instantiate the optimization algorithm
# IMGAMO parameters:
#                   population_size=50,
#                   exchange_iter=1,
#                   change_iter=1,
#                   clone_number=25,
#                   sup_level_f=0.1,
#                   sup_level_x=0.01,
#                   generator=RandomGenerator(),
#                   mutate=MutateIMGAMOHiper(),
#                   exchange_repair=None,
#                   dominance=ParetoDominance(),

algorithm = IMGAMO(problem, population_size=15, change_iter=1, clone_number=10, sup_level_f=0.10,
                   mutate=MutateIMGAMOHiper())

# optimize the problem using 10,000 function evaluations
st = time.process_time()
algorithm.run(10000)
print(time.process_time() - st)

print(algorithm.nfe)
print(algorithm.local_nfe)
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
