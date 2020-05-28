#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:15:43 2020

@author: jameselijah
"""

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

I.nx.MultiDiGraph() #This is directed multigraph


