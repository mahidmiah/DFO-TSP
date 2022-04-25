import matplotlib.pyplot as plt
import numpy as np
import collections
import random

def update(swarm, bestNeighbourTable, fitnessTable, delta, citiesObj, visualise, swarmNumber = 0):

    bestFly = np.argmin(fitnessTable)
    cities = [i for i in range(len(swarm[0]))]

    def mainUpdate(fly):
        bestNeighbour = bestNeighbourTable[fly]

        def is_fly_valid():
            if len(set(swarm[fly])) == len(swarm[fly]):
                return True
            return False

        def update_dimensions():
            for dimension in range(len(swarm[fly])):  # Loops through each dimension within the flies solution.
                # Original disturbance threshold code.
                if np.random.rand() < delta:
                    swarm[fly][dimension] = np.random.choice(cities)
                    continue

                # Updates the flies current dimension in loop.
                u = np.random.rand()
                swarm[fly][dimension] = int(swarm[bestNeighbour][dimension] + u * (swarm[bestFly][dimension] - swarm[fly][dimension]))

                # OUT OF BOUND CONTROL FOR DIMENSION
                if swarm[fly][dimension] not in cities:
                    swarm[fly][dimension] = random.choice([i for i in cities if i not in swarm[fly]])

        update_dimensions()

        # OUT OF BOUND CONTROL FOR FLY - forces
        if not is_fly_valid():
            missingDimensions = [dim for dim in cities if dim not in swarm[fly]]
            duplicateDimensions = [(dim, count) for dim, count in collections.Counter(swarm[fly]).items() if count > 1]
            for dimension in duplicateDimensions:
                if dimension[1] == 1:
                    swarm[fly][swarm[fly].index(dimension[0])] = missingDimensions.pop()
                else:
                    for i in range(dimension[1] - 1):
                        swarm[fly][swarm[fly].index(dimension[0])] = missingDimensions.pop()



    for fly in range(len(swarm)):
        if fly == bestFly: continue  # ELITIST STRATEGY
        mainUpdate(fly)

        if visualise == True:

            def get_fly_coordinates(fly):
                x = []
                y = []
                for dimension in range(len(swarm[fly])):
                    if dimension != len(swarm[fly]) - 1:
                        nextFly = swarm[fly][dimension + 1]
                    else:
                        nextFly = swarm[fly][0]
                    currentFly = swarm[fly][dimension]
                    for city in citiesObj:
                        if city.node == currentFly:
                            x.append(city.x)
                            y.append(city.y)
                            for edge in city.edges:
                                if edge['linkedNode'] == nextFly:
                                    x.append(edge['x'])
                                    y.append(edge['y'])
                return x, y

            bestX, bestY = get_fly_coordinates(bestFly)
            plt.gca().add_line(plt.Line2D(bestX, bestY, color="blue", linewidth=2.5))

            if fly % 5 == 0:
                x, y = get_fly_coordinates(fly)
                for val in x:
                    plt.gca().add_line(plt.Line2D(x, y, color="orange", linewidth=0.75, linestyle='-'))
                plt.title(f"Swarm: {swarmNumber} - Fly Value: {fly}")
                plt.axis('auto')
                plt.pause(0.0001)
                plt.clf()




