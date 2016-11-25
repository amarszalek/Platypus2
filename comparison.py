import six
from platypus.algorithms import *
from platypus.problems import DTLZ2
from platypus.experimenter import experiment
from platypus.evaluator import ProcessPoolEvaluator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    # setup the experiment
    problem = DTLZ2(3)

    imgamo_par = {"population_size": 20, "change_iter": 1, "clone_number": 10, "sup_level_f": 0.10, "sup_level_x": 0.01}

    algorithms = [NSGAII,
                  (NSGAIII, {"divisions_outer":12}),
                  (CMAES, {"epsilons":[0.05]}),
                  GDE3,
                  IBEA,
                  MOEAD,
                  (OMOPSO, {"epsilons":[0.05]}),
                  SMPSO,
                  SPEA2,
                  (EpsMOEA, {"epsilons":[0.05]}),
                  (IMGAMO, imgamo_par)]
    
    # run the experiment using Python 3's concurrent futures for parallel evaluation
    with ProcessPoolEvaluator() as evaluator:
        results = experiment(algorithms, problem, seeds=1, nfe=10000, evaluator=evaluator)

    # display the results
    fig = plt.figure()
    
    for i, algorithm in enumerate(six.iterkeys(results)):
        result = results[algorithm]["DTLZ2"][0]
        
        ax = fig.add_subplot(3, 4, i+1, projection='3d')
        ax.scatter([s.objectives[0] for s in result],
                   [s.objectives[1] for s in result],
                   [s.objectives[2] for s in result])
        ax.set_title(algorithm)
        ax.set_xlim([0, 1.1])
        ax.set_ylim([0, 1.1])
        ax.set_zlim([0, 1.1])
        ax.view_init(elev=30.0, azim=15.0)
        ax.locator_params(nbins=4)
    
    plt.show()
