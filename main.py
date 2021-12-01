from city_generator.generator import generateCities
from plotter.plot_cities import plot
from DFO.generate_swarm import generateSwarm
from DFO.DFO import DFO

cities, distanceTable = generateCities(100, 0, 1000)
startCity = 2

swarm = generateSwarm(100, len(cities), startCity)
bestPath = DFO(maxIterations=3000, swarm=swarm, distanceTable=distanceTable, startNode=startCity, delta=0.0009)
plot(cities, [bestPath], distanceTable, 1)