import numpy as np

def generateSwarm(population, dimensionality):
    swarm = [[0 for i in range(dimensionality)] for j in range(population)]

    for i in range(population):
        fly = [i for i in range(dimensionality)]
        np.random.shuffle(fly)
        swarm[i] = fly

    return swarm