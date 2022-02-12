import collections
import random
import numpy as np

def update(swarm, bestNeighbourTable, fitnessTable, delta, startNode):

    bestFly = np.argmin(fitnessTable)
    cities = [i for i in range(len(swarm[0]))]

    def mainUpdate(fly):
        bestNeighbour = bestNeighbourTable[fly]

        for dimension in range(len(swarm[fly])):

            # Original disturbance threshold code.
            if np.random.rand() < delta:
                swarm[fly][dimension] = random.choice(cities)
                continue

            u = np.random.rand()
            swarm[fly][dimension] = int(swarm[bestNeighbour][dimension] + u * (swarm[bestFly][dimension] - swarm[fly][dimension]))

            # OUT OF BOUND CONTROL FOR DIMENSION
            if swarm[fly][dimension] not in cities:
                swarm[fly][dimension] = random.choice([i for i in cities if i not in swarm[fly]])

        # OUT OF BOUND CONTROL FOR FLY
        missingDimensions = [dim for dim in cities if dim not in swarm[fly]]
        duplicateDimensions = [(dim, count) for dim, count in collections.Counter(swarm[fly]).items() if count > 1]

        for dimension in duplicateDimensions:
            if dimension[1] == 1:
                swarm[fly][swarm[fly].index(dimension[0])] = missingDimensions.pop()
            else:
                for i in range(dimension[1] - 1):
                    swarm[fly][swarm[fly].index(dimension[0])] = missingDimensions.pop()

        # Re-inserts the start node at the front.
        swarm[fly].remove(startNode)
        swarm[fly].insert(0, startNode)

    for fly in range(1, len(swarm)):
        if fly == bestFly: continue  # ELITIST STRATEGY
        mainUpdate(fly)

