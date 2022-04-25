import multiprocessing as mp
from city_generator.generator import generateCities
from plotter.plot_cities import plot
from DFO.generate_swarm import generateSwarm
from DFO.DFO import DFO

def runAlgorithm(dataset, swarmSize = 800, maximumIterations = 9000, disturbanceThreshold = 0.001, multipleSwarmsApproach = True, numberOfSwarms = 5, visualise = False):

    cities, distanceTable = generateCities(dataset)
    queue = mp.Queue()  # Multiprocessing queues.

    # Multiple Swarms Approach:
    if multipleSwarmsApproach == True:

        swarms = [] # List of swarms.
        processes = [] # List of multiprocessing processes.
        results = [] # List of outputted results from all swarms.

        # Generates specified number of swarms.
        for i in range(numberOfSwarms):
            # Creates swarm.
            swarms.append(generateSwarm(swarmSize, len(cities)))
            # Creates multiprocessing DFO process for the generated swarm.
            # Arguments in order: Max iterations, swarm, distance table, disturbance threshold, cities, multiprocessing, mp.queue, swarm number, visualise.
            processes.append(mp.Process(target=DFO, args=(maximumIterations, swarms[i], distanceTable, disturbanceThreshold, cities, True, queue, i, visualise)))

        # Starts each multiprocessing process.
        for process in processes:
            process.start()

        # Get Swarm/DFO output from the multiprocessing queue.
        for i in range(len(swarms)):
            results.append(queue.get())

        # Find the best outputted results from all the swarms used.
        fitnessValues = []
        for result in results:
            fitnessValues.append(result[1])
        bestResultIndex = fitnessValues.index(min(fitnessValues))

        # Display the optimal route details.
        print(f"\nSwarm: {results[bestResultIndex][2]}")
        print(f"Optimal route: {results[bestResultIndex][0]}")
        print(f"Fitness value: {results[bestResultIndex][1]}")

        # Plot the solution
        plot(cities, [results[bestResultIndex][0]], distanceTable, True, [results[bestResultIndex][1]])

    # Without the Multiple Swarms Approach.
    else:
        # Generates the swarm.
        swarm = generateSwarm(swarmSize, len(cities))
        # Find optimal path.
        bestPath = DFO(maxIterations = maximumIterations, swarm = swarm, distanceTable = distanceTable, delta = disturbanceThreshold, cities = cities, multiProcessing = False, queue = queue, visualise=visualise)
        # Plot the solution.
        plot(cities, [bestPath[0]], distanceTable, True, [bestPath[1]])

if __name__ ==  '__main__':
    runAlgorithm("TSPs/wi29.tsp")
