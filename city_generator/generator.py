import numpy as np
from city_generator.city import city
from multipledispatch import dispatch

@dispatch(int,int,int)
def generateCities(numOfCities, lowerBound, upperBound):
    np.random.seed(19680801)
    cities = []
    distanceTable = [[0 for i in range(numOfCities)] for j in range(numOfCities)]

    for i in range(numOfCities):
        cityObj = city(i, np.random.randint(lowerBound,upperBound), np.random.randint(lowerBound,upperBound))
        cities.append(cityObj)

    for i in range(len(cities)):
        for node in cities:
            if i != node.node:
                edge = {"linkedNode": node.node, "x": node.x, "y": node.y, "distance": ( abs(cities[i].x - node.x) + abs(cities[i].y - node.y) )}
                cities[i].edges.append(edge)

    for i in range(0, len(cities)):
        for j in range(0, len(cities)-1):
            distanceTable[cities[i].node][cities[i].edges[j]['linkedNode']] = cities[i].edges[j]['distance']

    return cities, distanceTable

@dispatch(str)
def generateCities(TSPfile):

    file = open(TSPfile, "r")

    lines = file.readlines()
    formatted_lines = []
    for line in lines:
        formatted_lines.append(line.rstrip("\n"))

    TSP_dimension = int(formatted_lines[4].split(" ")[2])
    counter = 7  # The first node of the TSP starts on line 7.
    EOF = counter + TSP_dimension

    TSP_nodes = []
    while counter < EOF:
        node = []
        for value in formatted_lines[counter].split(" "):
            node.append(float(value))
        TSP_nodes.append(node)
        counter += 1

    cities = []
    distanceTable = [[0 for i in range(TSP_dimension)] for j in range(TSP_dimension)]

    for i in range(TSP_dimension):
        cityObj = city(i, TSP_nodes[i][1], TSP_nodes[i][2])
        cities.append(cityObj)

    for i in range(len(cities)):
        for node in cities:
            if i != node.node:
                edge = {"linkedNode": node.node, "x": node.x, "y": node.y, "distance": ( abs(cities[i].x - node.x) + abs(cities[i].y - node.y) )}
                cities[i].edges.append(edge)

    for i in range(0, len(cities)):
        for j in range(0, len(cities)-1):
            distanceTable[cities[i].node][cities[i].edges[j]['linkedNode']] = cities[i].edges[j]['distance']

    return cities, distanceTable
