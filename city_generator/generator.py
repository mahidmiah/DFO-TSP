import numpy as np
from city_generator.city import city

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
            # print(f"Node: {cities[i].node}, Linked node: {cities[i].edges[j]['linkedNode']}")
            distanceTable[cities[i].node][cities[i].edges[j]['linkedNode']] = cities[i].edges[j]['distance']

    # print(f"Distance Table:\n        {[[col] for col in range(len(distanceTable))]}")
    # for row in range(len(distanceTable)):
    #     print(f"Row: {[row]} {distanceTable[row]}")

    return cities, distanceTable
