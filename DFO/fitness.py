def fit(swarm, distanceTable):
    fitnessTable = []

    def f(fly):
        fitness = 0
        for dimension in range(len(fly)): # Loops through each dimension in the fly/solution.
            if dimension != len(fly) - 1: # Checks if the dimension is the last dimension in the fly/solution.
                currentDimension = fly[dimension]
                nextDimension = fly[dimension + 1]
                cost = distanceTable[currentDimension][nextDimension] # Gets the cost from the distanceTable (based on Euclidean Distance).
                fitness = fitness + cost # Appends the cost
            else: # Runs if the dimension is the last dimension in the fly/solution.
                currentDimension = fly[dimension]
                nextDimension = fly[0]
                cost = distanceTable[currentDimension][nextDimension] # Gets the cost from the distanceTable (based on Euclidean Distance).
                fitness = fitness + cost # Appends the cost.

        return fitness

    # Calls the 'f' function on each fly in the loop and saves the cost/fitness value in the fitnessTable.
    for fly in swarm:
        fitnessTable.append(f(fly))

    return fitnessTable
