import numpy as np 
import networkx as nx

def load_data(filename="../data/day15_test.txt"):
    cave = list()
    for line in open(filename,"r").readlines():
        line = [int(x) for x in line.rstrip()]
        cave.append(line)
    return np.array(cave)

def generate_graph():
    g = nx.DiGraph()
    for x in range(MAP.shape[0]):
        for y in range(MAP.shape[1]):
            for x1,y1 in STEPS:
                if (-1 < x+x1 < MAP.shape[0]) and (-1 < y+y1 < MAP.shape[1]):
                    w = MAP[x+x1,y+y1]
                    g.add_edge((x,y), (x+x1,y+y1), weight=w)
    return g

MAP = load_data("../data/day15_input.txt")

STEPS = [(1,0),(0,1),(-1,0),(0,-1)]
g = generate_graph()
END = (MAP.shape[0]-1,MAP.shape[1]-1)
path = nx.shortest_path(g, 
                        (0, 0), 
                        END, 
                        weight="weight",
                        method="dijkstra")
score = nx.shortest_path_length(g, (0, 0), END, weight="weight")
print(score)