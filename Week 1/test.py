import networkx as nx

G=nx.MultiGraph()
G.add_node('A',role='manager')
G.add_edge('A','B',relation = 'friend')
G.add_edge('A','C', relation = 'business partner')
G.add_edge('A','B', relation = 'classmate')
G.node['A']['role'] = 'team member'
G.node['B']['role'] = 'engineer'

#P = G.get_edge_data("A", "B")[0]
#node = G.number_of_edges()
P = G.edge()

#print (node)