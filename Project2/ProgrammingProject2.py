#Social Network Graphical Representation
#Author: Jewels Wolter
#Course: COMP 3270

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

#Implement BFS

#Implement DFS

#Generate a report for distance and time taken for BFS and DFS
 
#Main function
print(createGraph(getEdges('Test_Case_Assignment2.txt')))