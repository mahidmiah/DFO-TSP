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
                fitness = fitness + cost ** 2
            else:
                currentDimension = fly[dimension]
                nextDimension = fly[0]
                cost = distanceTable[currentDimension][nextDimension]
                fitness = fitness + cost ** 2

        return np.sqrt(fitness)

    for fly in swarm:
        fitnessTable.append(f(fly))

    return fitnessTable

# def fit(swarm, distanceTable):
#     fitnessTable = []
#
#     def f(fly):
#         fitness = 0
#         for dimension in range(len(fly)):
#             if dimension != len(fly) - 1:
#                 currentDimension = fly[dimension]
#                 nextDimension = fly[dimension + 1]
#                 cost = distanceTable[currentDimension][nextDimension]
#                 fitness = fitness + cost
#             else:
#                 currentDimension = fly[dimension]
#                 nextDimension = fly[0]
#                 cost = distanceTable[currentDimension][nextDimension]
#                 fitness = fitness + cost
#
#         return fitness
#
#     for fly in swarm:
#         fitnessTable.append(f(fly))
#
#     return fitnessTable
