import random


def generateSwarm(population, dimensionality, startNode):
    swarm = [[0 for i in range(dimensionality)] for j in range(population)]

    for i in range(population):
        fly = [i for i in range(dimensionality)]
        random.shuffle(fly)
        fly.remove(startNode)
        fly.insert(0, startNode)
        swarm[i] = fly

    return swarm