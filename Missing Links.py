import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodeList = []
edgeList = []
nodeCnt = {}

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

def Random_Walk(graph):

    random_node = random.choice(nodeList)

    for i in range(100000):
        n = random.random()  
        nodeCnt[random_node] += 1  
        if(list(Graph.neighbors(random_node)) == [] or n < 0.15):
            random_node = random.choice(nodeList)
            continue
        random_node = random.choice(list(Graph.neighbors(random_node)))

    sorted_nodeList = dict(sorted(nodeCnt.items(), key=lambda item: item[1], reverse=True))
    print("the top leader is:", list(sorted_nodeList.keys())[0])  
    return sorted_nodeList  

def linkAnalysis(adj_mat, node1, node2):

    B = np.delete(adj_mat[node1], node2)
    C = np.delete(adj_mat[:, node2], node1)
    A = np.delete(adj_mat, node1, axis=0)
    A = np.delete(A, node2, axis=1)
    X, residuals, _, _ = np.linalg.lstsq(A.T, B, rcond=None)

    return np.dot(X, C)

def missingLinkAnalysis():
    missing_Link = []
    c = 0  
    
    adj_mat = nx.adjacency_matrix(Graph).todense()

    pagerank = Random_Walk(Graph)
    pagerankKey_list = list(pagerank.keys())
    nodeList = list(nx.nodes(Graph))
    n = len(nodeList)

    for i in range(n):
        if(np.all(adj_mat[i] == 0)):
            for k in range(n):
                prob = .1 + .4*(1 - pagerankKey_list.index(nodeList[k])/(n-1))
                x = random.random()
                if(x <= prob):

                    adj_mat[i][k] = 1
                    c += 1
                    missing_Link.append((nodeList[i], nodeList[k]))
                    print("Missing Link :", nodeList[i], '-', nodeList[k])
            continue
        for j in range(n):
            if(adj_mat[i][j] == 1 or i == j):
                continue
            a = linkAnalysis(adj_mat, i, j)
            if(a > 0):
                a = 1
            if(a == 1):
                c += 1
                missing_Link.append((nodeList[i], nodeList[j]))
                print("Missing Link :", nodeList[i], '-', nodeList[j])
            adj_mat[i, j] = a
    print("Total number of missing links predicted : ", c)
    return adj_mat

missingLinkAnalysis()