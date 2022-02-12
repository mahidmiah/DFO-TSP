
def findBestNeighbour(swarm, fitnessTable):
    bestNeighbourTable = []

    for fly in range(len(swarm)):
        if fly != len(swarm)-1:
            leftFly = fly-1
            rightFly = fly+1

            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)
        else:
            leftFly = fly - 1
            rightFly = 0

            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)

    return bestNeighbourTable

