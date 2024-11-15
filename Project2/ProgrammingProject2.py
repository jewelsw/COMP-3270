#Social Network Graphical Representation
#Author: Jewels Wolter
#Course: COMP 3270
#Used Copilot in VSCode to help with code generation

#Import necessary libraries
import time

#Parse edges from the file
def getEdges(filename):
    edges = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            node1, node2 = line.split(',')
            edges.append((node1, node2))
    return edges

#Create a graph from the edges
def createGraph(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

#Implement BFS (Breadth First Search) algorithm 
#Output - Distance for each node from node 1 to 24 and time taken 
def BFS(graph, start):
    #Define local variables
    visited = []
    queue = []
    times = {}
    distances = {}

    #Initialize the queue
    queue.append(start)
    visited.append(start)
    distances[start] = 0
    
    #Start the timer
    start_time = time.time()
    times[start] = 0
    
    #Iterate through the graph
    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                distances[neighbour] = len(visited)
                times[neighbour] = (time.time() - start_time) * 1000
                      
    return distances, times

#Implement DFS
def DFS(graph, start):
    #Define local variables
    visited = []
    stack = []
    times = {}
    distances = {}

    #Initialize the stack
    stack.append(start)
    visited.append(start)
    distances[start] = 0
    
    #Start the timer
    start_time = time.time()
    times[start] = 0
    
    #Iterate through the graph
    while stack:
        node = stack.pop()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
                distances[neighbour] = len(visited)
                times[neighbour] = (time.time() - start_time) * 1000 
                      
    return distances, times

#Generate a report for distance and time taken for BFS and DFS
 
#Main function
edges = getEdges('Test_Case_Assignment2.txt')
graph = createGraph(edges)

print('BFS Report')
BFSDistances, BFSTime = BFS(graph, 'N_0')
for node, distance in BFSDistances.items():
    print(f'{node} - {distance} nodes visited in {BFSTime[node]} ms from N_0')

print('\nDFS Report')
DFSDistances, DFSTime = DFS(graph, 'N_0')
for node, distance in DFSDistances.items():
    print(f'{node} - {distance} nodes visitied in {DFSTime[node]} ms from N_0')