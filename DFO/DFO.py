from DFO.fitness import fit
from DFO.best_neighbour import findBestNeighbour
from DFO.update import update
import numpy as np
import time

def DFO(maxIterations, swarm, distanceTable, delta, cities, multiProcessing, queue, swarmNumber = 0, visualise = False):

    overallFitness = []
    start_time = time.time()

    for iteration in range(maxIterations):
        fitnessTable = fit(swarm, distanceTable) # Evaluates the whole swarm
        bestNeighbourTable = findBestNeighbour(swarm, fitnessTable)  # Finds each Flies best neighbour.

        if iteration % 100 == 0:
            print(f"     Swarm: {swarmNumber}, Iteration {iteration}, Best fly index: {np.argmin(fitnessTable)}, Fitness Value: {fitnessTable[np.argmin(fitnessTable)]}, Delta Value: {delta}")

        if visualise == True:
            if iteration % 250 == 0:
                update(swarm, bestNeighbourTable, fitnessTable, delta, cities, True, swarmNumber)  # Updates the whole swarm - Shows visualiastion.
            else:
                update(swarm, bestNeighbourTable, fitnessTable, delta, cities, False, swarmNumber)  # Updates the whole swarm - Disables the visualisation to only show every 250 iterations.
        else:
            update(swarm, bestNeighbourTable, fitnessTable, delta, cities, False, swarmNumber)  # Updates the whole swarm - Without visualisation.
        overallFitness = fitnessTable

    print()
    print(f"     Swarm: {swarmNumber}")
    print(f"     Final best fitness: {overallFitness[np.argmin(overallFitness)]}")
    print(f"     Final best fly: {swarm[np.argmin(overallFitness)]}")
    print("     --- %s seconds ---" % (time.time() - start_time))
    print()

    # If the Multiple Swarms Approach is used then the outputted results will be put into the queue.
    if multiProcessing == True:
        queue.put([swarm[np.argmin(overallFitness)], overallFitness[np.argmin(overallFitness)], swarmNumber])

    return [swarm[np.argmin(overallFitness)], overallFitness[np.argmin(overallFitness)], swarmNumber]