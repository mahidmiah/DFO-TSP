from city_generator.generator import generateCities
from plotter.plot_cities import plot
from DFO.generate_swarm import generateSwarm
from DFO.DFO import DFO
import time





cities, distanceTable = generateCities("TSPs/wi29.tsp")
startCity = 2

swarm = generateSwarm(275, len(cities), startCity)
bestPath = DFO(maxIterations=25000, swarm=swarm, distanceTable=distanceTable, startNode=startCity, delta=0.001)
plot(cities, [bestPath], distanceTable, 1)
