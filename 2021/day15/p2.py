import numpy as np 
import networkx as nx
from copy import deepcopy 

def load_data(filename="../data/day15_test.txt"):
    cave = list()
    for line in open(filename,"r").readlines():
        line = [int(x) for x in line.rstrip()]
        cave.append(line)
    cave = np.array(cave)
    return cave

def generate_graph():
    g = nx.DiGraph()
    for x in range(MAP.shape[0]):
        for y in range(MAP.shape[1]):
            for x1,y1 in STEPS:
                if (-1 < x+x1 < MAP.shape[0]) and (-1 < y+y1 < MAP.shape[1]):
                    w = MAP[x+x1,y+y1]
                    g.add_edge((x,y), (x+x1,y+y1), weight=w)
    return g

def expand_map(M,n=5):
    megamap = np.zeros((M.shape[0]*5,M.shape[1]*5))
    xw,yw = M.shape
    for xi in range(0,5):
        for yi in range(0,5):
            newmap = deepcopy(M)
            newmap += yi + xi
            newmap[newmap>9] = newmap[newmap>9]-9
            megamap[yw*yi:yw+(yw*yi),xw*xi:xw+(xw*xi)] = newmap
    return megamap
        


MAP = load_data("../data/day15_input.txt")
MAP=expand_map(MAP)

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