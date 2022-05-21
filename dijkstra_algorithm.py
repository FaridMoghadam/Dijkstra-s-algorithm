from math import inf
from copy import deepcopy

graph = {
    'A':{'B':20, 'D':5, 'C':5},
    'B':{'A':20, 'C':5, 'D':6},
    'C':{'A':5, 'B':5},
    'D':{'A':5, 'B':6},}

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = deepcopy(graph)
    infinity = inf
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
        
        print (shortest_distance)
        
    shortest_distance[start] = 0

    # Determine which is minimum node. What does that mean?
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
                print ("minNode: ", minNode)
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for edge, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[edge]:
                shortest_distance[edge] = weight + shortest_distance[minNode]
                predecessor[edge] = minNode
                print ("predecessor: ", predecessor)
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
            
            print ("currentNode: ", predecessor)
            
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('----------------------------------------- ')
        print('Shortest distance is = ' + str(shortest_distance[goal]))
        print('And the Best path is ' + str(path))
        print('----------------------------------------- ')


# How TO Use this Code 
## Write the first point and the last point as follows :
## dijkstra(graph, 'A', 'B')
## dijkstra(graph, 'D', 'C')
        
