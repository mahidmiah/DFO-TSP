
def findBestNeighbour(swarm, fitnessTable):
    bestNeighbourTable = []

    # Loops through each fly in the swarm
    for fly in range(len(swarm)):
        if fly != len(swarm)-1: # Checks if the fly is the last fly
            leftFly = fly-1
            rightFly = fly+1

            # Decides the best neighbour and appends result to the table
            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)
        else: # Runs if the fly in loop is the last fly in the swarm
            leftFly = fly - 1
            rightFly = 0

            # Decides the best neighbour and appends result to the table
            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)

    return bestNeighbourTable

