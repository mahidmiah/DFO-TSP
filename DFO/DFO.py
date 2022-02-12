from DFO.fitness import fit
from DFO.best_neighbour import findBestNeighbour
from DFO.update import update
import numpy as np
import time

def DFO(maxIterations, swarm, distanceTable, startNode, delta = 0.001):

    overallFitness = []

    start_time = time.time()
    for iteration in range(maxIterations):
        fitnessTable = fit(swarm, distanceTable)

        if iteration % 100 == 0:
            print(f"Iteration {iteration}, Best fly: {np.argmin(fitnessTable)}, Fitness Value: {fitnessTable[np.argmin(fitnessTable)]}")

        bestNeighbourTable = findBestNeighbour(swarm, fitnessTable)
        update(swarm, bestNeighbourTable, fitnessTable, delta, startNode)
        overallFitness = fitnessTable

    print()
    print(f"Final best fitness: {overallFitness[np.argmin(overallFitness)]}")
    print(f"Final best fly: {swarm[np.argmin(overallFitness)]}")

    print("--- %s seconds ---" % (time.time() - start_time))
    return swarm[np.argmin(overallFitness)]