import matplotlib.pyplot as plt
from datetime import datetime

def plot(cities, swarm, distanceTable, showAllEdges, fitnessValue):

    # Plots all the cities/nodes on the graph.
    for city in cities:
        plt.scatter(city.x, city.y, label=f"City: {city.node}", s=20, zorder=5)

    # Shows the 'grey' lines in the outputted solution graph which are all the possible paths/routes that can be taken.
    for city in cities:
        for edge in city.edges:
            plt.plot((city.x, edge['x']), (city.y, edge['y']), c='lightgrey')

    # Shows the solution path/route.
    if showAllEdges == True:
        for fly in range(len(swarm)):
            for dimension in range(len(swarm[fly])):
                if dimension != len(swarm[fly]) - 1:
                    x = []
                    y = []
                    currentFly = swarm[fly][dimension]
                    nextFly = swarm[fly][dimension + 1]
                    for city in cities:
                        if city.node == currentFly:
                            x.append(city.x)
                            y.append(city.y)
                            for edge in city.edges:
                                if edge['linkedNode'] == nextFly:
                                    x.append(edge['x'])
                                    y.append(edge['y'])
                    plt.plot(x, y, label=f"Distance/Cost: {distanceTable[currentFly][nextFly]}", linewidth=2.5)
                else:
                    x = []
                    y = []
                    currentFly = swarm[fly][dimension]
                    nextFly = swarm[fly][0]
                    for city in cities:
                        if city.node == currentFly:
                            x.append(city.x)
                            y.append(city.y)
                            for edge in city.edges:
                                if edge['linkedNode'] == nextFly:
                                    x.append(edge['x'])
                                    y.append(edge['y'])
                    plt.plot(x, y, label=f"Distance/Cost: {distanceTable[currentFly][nextFly]}", linewidth=2.5)

    plt.title(f"Fitness Value: {fitnessValue} \nSwarm: {swarm}")

    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', ncol=5)
    plt.tight_layout()

    # Saves the solution figure into the 'Outputs' folder.
    plt.savefig("Outputs/" + str(datetime.now().strftime("[%d-%m-%Y] [%H-%M-%S]")) + ".png")

    # Displays the solution.
    plt.show()