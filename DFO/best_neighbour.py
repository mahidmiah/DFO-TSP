
def findBestNeighbour(swarm, fitnessTable):
    bestNeighbourTable = []

    for fly in range(len(swarm)):
        if fly != len(swarm)-1:
            currentFly = fly
            leftFly = fly-1
            rightFly = fly+1

            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)
        else:
            currentFly = fly
            leftFly = fly - 1
            rightFly = 0

            bestNeighbour = rightFly if fitnessTable[rightFly] < fitnessTable[leftFly] else leftFly
            bestNeighbourTable.append(bestNeighbour)

    # print("Best Neighbour:")
    # for fly in range(len(swarm)):
    #     bestPosition = "right" if fly < bestNeighbourTable[fly] else "left"
    #     print(f"Fly {fly}: {swarm[fly]} --> Best neighbour (index): {bestNeighbourTable[fly]} ({bestPosition})")
    # print()

    return bestNeighbourTable
