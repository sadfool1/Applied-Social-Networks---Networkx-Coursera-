#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:15:43 2020

@author: jameselijah
"""
import numpy as np
import pandas as pd

import networkx as nx

G = nx.DiGraph()

"Adding Attribute"
G.add_edge ("A", "B", sign = "+", weight = 6) # attribute weight
G.add_edge ("B", "C", sign = "-") #signed networks "-" declaration of enemy or foe
G.add_edge ("C", "D", sign = "+", relation = "friend")#Other edge attributes i.e friend, fami, coworker

#Multigraphs: Network where multiple edges can connect the same nodes (parrallel edges)

H = nx.MultiGraph()
H.add_edge("A", "B", relation = "friend")
H.add_edge("A", "B", relation = "neighbour")

#ACCESSING ATTRIBUTES OF A SPECIFC EDGE
#H.edge["A"]["B"] --> ORDER does not matter i.e syntax.[B][A] = syntax.[A][B] However this does not work for directed weighted network
#OUT : {"relation": "family", "weight": 6}

#I.nx.MultiDiGraph() #This is directed multigraph

"""
Bipartite Graph: a graph whose nodes can be split into 
2 sets L & R and every edge connects a node in L with 
a node in R.
"""

from networkx.algorithms import bipartite

B = nx.Graph() #no separate class for bipartite graphs
B.add_nodes_from (["A","B", "C", "D"], bipartite = 0) #LABEL ONE SET OF NODES ()
B.add_nodes_from([1,2,3,4], bipartite = 1) #label other set of nodes 1
B.add_edges_from ([("A",1),("B",1),("C",1), ("C", 3), ("D",2),("E", 3), ("E", 4)])

print (bipartite.is_bipartite(B)) #query if B is bipartite
B.add_edge("A", "B") #this breaks the bipartition and returns False in the next line
print (bipartite.is_bipartite(B))
B.remove_edge("A", "B") #removes the edge
print (bipartite.is_bipartite(B))

X = set([1,2,3,4])
print (bipartite.is_bipartite_node_set(B,X)) #check if this set is in B
X = set(["A","B","C","D","E"])
print (bipartite.is_bipartite_node_set(B,X)) #check if this set is in B

## PROJECT GRAPH

##Bipartitd weighted graph projection 


"""
==========================================================
Ex. Use NetworkX to construct the bipartite weighted graph 
projection of nodes A,B,C,D,E,F and find the weight of 
the edge (A,C).

What is the weight of the edge (A,C)?
==========================================================
"""
import networkx as nx
from networkx.algorithms import bipartite

B = nx.Graph()
B.add_edges_from([('A', 'G'),('A','I'), ('B','H'), ('C', 'G'), ('C', 'I'),('D', 'H'), ('E', 'I'), ('F', 'G'), ('F', 'J')])
X1 = set(['A', 'B', 'C', 'D', 'E', 'F'])
P = bipartite.weighted_projected_graph(B,X1)
print (P.get_edge_data("A", "C"))

nx.draw_networkx(B)