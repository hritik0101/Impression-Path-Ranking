# Impression-Path-Ranking
This project implements a graph-based analysis for identifying influential nodes in a network and predicting missing links. It utilizes random walk algorithms and link analysis to rank nodes and simulate missing connections in a directed graph.

# Features:
Graph Creation from CSV: Builds a directed graph by parsing data from a CSV file, where nodes represent entities, and edges represent relationships.

Random Walk Simulation: Performs a random walk on the graph to simulate the movement of influence across the network. The result is a ranking of nodes based on their "impression," or the number of times they are visited during the walk.

Link Analysis: Applies a least-squares method to evaluate missing links in the graph, predicting connections that could exist based on node relationships.

Missing Link Prediction: Uses probabilistic methods to predict and add missing links between unconnected nodes, enhancing network connectivity.

# Application:
Influence Analysis: Ranking nodes based on their influence in a network (e.g., social networks, communication systems).
Link Prediction: Enhancing existing networks by predicting potential missing connections that could improve network efficiency or accuracy.
