#!/usr/bin/env python
# encoding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
with open(r'topo.csv','r') as f:
    data = f.read().split('\n')
print data
G = nx.DiGraph()
def add_edges(s):
    list_res = s.split(',')
    if len(list_res) != 4:
        print list_res
    else:
        G.add_weighted_edges_from([(int(list_res[1]),int(list_res[2]),float(list_res[3]))])
for i in data:
    add_edges(i)
nx.draw(G,node_size=300,alpha=0.5)
plt.show()
nx.draw_networkx()