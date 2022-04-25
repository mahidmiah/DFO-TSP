# Dispersive Flies Optimisation (DFO) for solving the Travelling Salesman Problem (TSP)
### Name: Mahid Miah - Student ID: 001063915

In order to run the DFO algorithm on a TSP, please input the directory/location of the given TSP inside the 'runAlgorithm' 
function as its parameter. For example, to use the 'wi29' TSP dataset from the 'TSPS' directory you would do the following:

```python
if __name__ ==  '__main__':
    runAlgorithm("TSPs/wi29.tsp")
```

## Parameter options
The algorithm consists of various different paramters which include the following:

* **dataset** - this parameter is the location of the dataset that is being solved - **and has no default value**.
* **swarmSize** - the size of the swarm - **has the default value of 800**.
* **maximumIterations** - the maximum number of iterations the algorithm will run for - **has default value of 9000**.
* **disturbanceThreshold** - the disturbance threshold value for the swarm(s) - **has default value of 0.001**.
* **multipleSwarmsApproach** - the multiple swarms approach for resolving the local optimum trap, it can be either set 
  to True or False - **has the default value of True**.
* **numberOfSwarms** - the number of swarms that will be used to solve the given TSP (this parameter will only be used 
  if the previous parameter is set to True) - **has the default value of 5**.
* **visualise** - can either be set to True or False and allows for a live visual representation of the swarm solving 
  the given TSP, were every 250 iterations the swarm will be displayed in a graph, however it should be noted that this 
  visualisation feature does slow down the algorithm as it takes time to visualise the swarm, in addition, this feature 
  does work for the multiple swarms approach but is buggy - **has the default value of False**.
  
### Parameter options - example
In order to run the algorithm without the multiple swarms approach and also enable the visualisation feature you would do 
the following:

```python
if __name__ ==  '__main__':
    runAlgorithm("TSPs/wi29.tsp", multipleSwarmsApproach = False, visualise = True)
```

## Features

Other features that this algorithm/application supports include randomly generated TSPs, saving a visual 
representation of the final outputted solution from the algorithm in the form of an image file (.png file), a visualisation
feature to view the swarm live, and also a Multiple Swarms Approach.

### Multiple Swarms Approach
As mentioned above, the algorithm supports a Multiple Swarms Approach feature which is used to resolve the Local Optimum
Trap that the DFO algorithm suffers from. The Multiple Swarms Approach is simply were multiple swarms are used to solve 
the same given TSP, and the swarm with the best result will be returned. This feature by **default is enabled**, and used **5 swarms**.

In order to disable this feature you would simply set the MultipleSwarmsApproach to False:
```python
if __name__ ==  '__main__':
    runAlgorithm("TSPs/wi29.tsp", multipleSwarmsApproach = False)
```

Furthermore, in order to specify the number of swarms used by this feature you would do the following (Assuming the feature
is enabled):

```python
if __name__ ==  '__main__':
    runAlgorithm("TSPs/wi29.tsp", numberOfSwarms = 10)
```
Where in the example above, the number of swarms has been set to 10, meaning 10 different swarms will be used to solve the 
given TSP.

### Randomly generated TSPs
The application supports solving randomly generated TSPs based on an inputted number of nodes and also a upper and lower 
bounds for the search space. It should be noted that the application makes use of a 'seed' in order to ensure that when 
the same inputted nodes and bounds are used the same randomly generated TSP will be generated. In order use a randomly 
generated TSP you would call the algorithm by doing the following:

```python
if __name__ ==  '__main__':
    runAlgorithm([14, 0, 1000])
```

Were rather than a string location value of a TSP file being inputted, a list object is inputted with the number of nodes, 
lower bound, and upper bound. So in the example above, using the inputted parameters, a randomly generated TSP with 14 
nodes within the bounds of 0 and 1000 will be generated and solved by the algorithm.

### Saving outputted solutions

![alt text](https://i.imgur.com/dCdHFQf.png)

As mentioned above, the application also saves the outputted solution in the form a png image file in the 'Outputs' directory,
where each image file is saved using the following naming convention: "[DAY-MONTH-YEAR] [HOUR-MINUTE-SECOND].png"

The image above depicts an example of an outputted solution for a randomly generated TSP in the form of a png file.
As seen from the example image, the image shows the most optimal path using the coloured lines, the nodes are represented
by the coloured dots, and the grey lines represent all the possible different paths that can be taken between the various
nodes in the given TSP. The image also shows the given path/tour with its fitness value.

It should also be noted that the other available paramter options can also be used with randomly generated TSPs. For example
if you would like to run the algorithm using 10 swarms and also enable the visualisation feature you would do the following:

```python
if __name__ ==  '__main__':
    runAlgorithm([14, 0, 1000], numberOfSwarms = 10, visualise = True)
```

### Visualisation feature

As mentioned above, the algorithm/application also supports a visualisation feature where every 250 iterations the live swarm is 
visualised on a graph, as can be seen in the following example:

![alt text](https://i.imgur.com/rEbRwnb.gif)

In the example displayed above, the blue line represents the current most optimal path/route found by the DFO algorithm,
while the orange lines represent the different paths that are currently being tested. It should be noted that using this feature
slow down the algorithm/application, and it also **not recommended** to use with the Multiple Swarms Approach as it is buggy.

In order to use the visualisation feature, simply enable the feature by setting the 'visualise' parameter to True, for example:

```python
if __name__ ==  '__main__':
    runAlgorithm([14, 0, 1000], visualise = True)
```

## Packages used

This algorithm/application makes use of various different packages which include the following:

* **Numpy** - Which is used by the algorithm/application for mathematical calculations/procedures.
* **Matplotlib** - Which is used by the algorithm/application in order to plot/display any given solution on a graph, 
  used to show the live swarm, and also to save the final outputted solution in the 'Outputs' folder in the form of an image file.
* **Multiprocessing** - Which is used for the Multiple Swarms Approach in order to make multiple Swarm/DFO processes to run
  simultaneously.
* **MultipleDispatch** - Which is used for method/function overloading as Python does not support this by default, and is specifically
  used in the 'generator.py' class where the generateCities() method can either be overloaded with a list object or string value.
