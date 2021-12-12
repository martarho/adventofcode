from collections import defaultdict 


def load_connections(filename):
    CONNECTIONS = defaultdict(list)
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            stt,end = line.rstrip().split("-")
            CONNECTIONS[stt].append(end)
            CONNECTIONS[end].append(stt)
    return CONNECTIONS

def check_possibilities(new_step, path):
    path_count = [ path.count(s) == 2 for s in list(set(path)) if s.islower()]
    if ((new_step == "start") or 
        ((new_step.islower()) and 
        (new_step in path and any(path_count)))):
        return False
    return True


def get_routes(path,step, routes_explored):
    if step == "end":
        routes_explored.add(tuple(path))
        return routes_explored
    for s in CONNECTIONS[step]:
        if check_possibilities(s,path) is False:
            continue
        routes_explored = get_routes(path+[s],s,routes_explored)
        path 
    return routes_explored


CONNECTIONS = load_connections("../data/day12_input.txt")
routes_explored = set()
routes_explored = get_routes([], 'start', routes_explored)
print(len(routes_explored))