#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys
from parseStr import *

if len(sys.argv) != 2:
	sys.exit('Usage: drawNetwork.py <network>. The network usually contains spaces, so it should be quoted.')

weights = parse2d(sys.argv[1])
neurons = len(weights)

G = nx.DiGraph()
for i in xrange(neurons):
	G.add_node(i)

pos = {}
for i in xrange(neurons):
	r = 1.0
	thetaInDegrees = float(i) * (360/float(neurons))
	thetaInRadians = thetaInDegrees * 3.14159 / 180.0
	x = r * np.sin(thetaInRadians)
	y = r * np.cos(thetaInRadians)
	pos[i] = (x, y)
labels = {}
for i in xrange(neurons):
	labels[i] = str(i)

for i in xrange(neurons):
	for j in xrange(neurons):
		if weights[i][j] != 0:
			G.add_edge(i, j, weight=weights[i][j])
eexcit = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 1.0]
einhib = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == -1.0]

nx.draw_networkx_nodes(G, pos, node_size=600, node_color='w')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

nx.draw_networkx_edges(G, pos, edgelist=eexcit, width=2, alpha=0.5, edge_color='b')
nx.draw_networkx_edges(G, pos, edgelist=einhib, width=2, alpha=0.5, edge_color='r')

if len(G.selfloop_edges()) > 0:
	sys.stdout.write('Nodes with selfloops found:')
	for node in G.nodes_with_selfloops():
		sys.stdout.write(' ' + str(node))
	sys.stdout.write('. See simple.png for graphviz graph\n')
	B = nx.to_agraph(G)
	B.layout()
	B.draw('simple.png')

plt.axis('off')
plt.show()
