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

    imgamo_par1 = {"population_size": 20, "exchange_iter": 1, "change_iter": 1, "clone_number": 10, "sup_level_f": 0.10,
                   "sup_level_x": 0.01}
    imgamo_par2 = {"population_size": 25, "exchange_iter": 1, "change_iter": 1, "clone_number": 25, "sup_level_f": 0.10,
                   "sup_level_x": 0.01}
    imgamo_par3 = {"population_size": 25, "exchange_iter": 1, "change_iter": 3, "clone_number": 15, "sup_level_f": 0.10,
                   "sup_level_x": 0.01}
    imgamo_par4 = {"population_size": 25, "exchange_iter": 3, "change_iter": 3, "clone_number": 25, "sup_level_f": 0.10,
                   "sup_level_x": 0.01}
    imgamo_par5 = {"population_size": 25, "exchange_iter": 1, "change_iter": 1, "clone_number": 25, "sup_level_f": 0.10,
                   "sup_level_x": 0.0001}
    imgamo_par6 = {"population_size": 25, "exchange_iter": 1, "change_iter": 1, "clone_number": 25, "sup_level_f": 0.05,
                   "sup_level_x": 0.0001}

    algorithms = [(IMGAMO, imgamo_par1, "IMGAMO_1"),
                  (IMGAMO, imgamo_par2, "IMGAMO_2"),
                  (IMGAMO, imgamo_par3, "IMGAMO_3"),
                  (IMGAMO, imgamo_par4, "IMGAMO_4"),
                  (IMGAMO, imgamo_par5, "IMGAMO_5"),
                  (IMGAMO, imgamo_par6, "IMGAMO_6")]

    # run the experiment using Python 3's concurrent futures for parallel evaluation
    with ProcessPoolEvaluator() as evaluator:
        results = experiment(algorithms, problem, seeds=1, nfe=10000, evaluator=evaluator)

    # display the results
    fig = plt.figure()
    
    for i, algorithm in enumerate(six.iterkeys(results)):
        result = results[algorithm]["DTLZ2"][0]
        print(algorithm)
        print('nfe: ', results[algorithm]["DTLZ2"][1])
        print('iter: ', results[algorithm]["DTLZ2"][2])
        print('time: ', results[algorithm]["DTLZ2"][3])
        ax = fig.add_subplot(2, 3, i+1, projection='3d')
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
