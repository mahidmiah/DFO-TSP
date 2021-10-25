import numpy as np

def fit(swarm, distanceTable):

    fitnessTable = []

    def f(fly):
        fitness = 0
        for dimension in range(len(fly)):
            if dimension != len(fly)-1:
                currentDimension = fly[dimension]
                nextDimension = fly[dimension+1]
                cost = distanceTable[currentDimension][nextDimension]
                fitness = fitness + cost**2
            else:
                currentDimension = fly[dimension]
                nextDimension = fly[0]
                cost = distanceTable[currentDimension][nextDimension]
                fitness = fitness + cost ** 2
        return np.sqrt(fitness)

    for fly in swarm:
        fitnessTable.append(f(fly))

    # print("Fitness:")
    # for fly in range(len(swarm)):
    #     print(f"Fly {fly}: {swarm[fly]} --> Fitness: {fitnessTable[fly]}")
    # print()

    return fitnessTable
