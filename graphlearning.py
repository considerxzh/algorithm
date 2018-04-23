"""
leanrning how to use pygraphviz
"""
from pygraphviz import *
if __name__=="__main__":
    g = AGraph()
    g.add_node('a')
    g.add_edge('b', 'c')
    g.graph_attr['label'] = 'name of graph'
    g.node_attr['shape'] = 'circle'
    g.edge_attr['color'] = 'red'
    g.layout(prog='dot')
    g.draw('first_pygraphviz.jpg')