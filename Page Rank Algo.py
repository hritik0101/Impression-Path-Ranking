import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodeList = []
edgeList = []
nodeCnt = {}

# Function to create a graph from a CSV file
def From_CSV_To_Graph(fileName):

    file = open(fileName, 'r')

    data = csv.reader(file)
    next(data)  

    g = nx.DiGraph()

    for row in data:
        
        p1 = row[1][0:11].upper()
        nodeList.append(p1)  

        for i in row[2:]:
            if(i != ""):
                p2 = i[-11:].upper()
                nodeCnt[p2] = 0
                edgeList.append((p1, p2))


    g.add_nodes_from(nodeList)
    g.add_edges_from(edgeList)

    file.close()

    return g


Graph = From_CSV_To_Graph('impressionData.csv')

# Function to perform a random walk on the graph
def Random_Walk(graph):

    random_node = random.choice(nodeList)

    # Iterate through the random walk process
    for i in range(100000):
        n = random.random()  
        nodeCnt[random_node] += 1  
        if(list(Graph.neighbors(random_node)) == [] or n < 0.15):

            random_node = random.choice(nodeList)
            continue
        random_node = random.choice(list(Graph.neighbors(random_node)))

    sorted_nodeList = dict(sorted(nodeCnt.items(), key=lambda item: item[1], reverse=True))
    print("The top leader is:", list(sorted_nodeList.keys())[0])  
    return sorted_nodeList  

Random_Walk(Graph)