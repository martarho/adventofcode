from itertools import product
from collections import defaultdict

def load_file(filename):
    coords = []
    for line in open(filename, 'r'):
        xy1,xy2 = line.rstrip().split(" -> ")
        coord_tuple = [
            [int(i) for i in xy1.split(",")],
            [int(i) for i in xy2.split(",")]
        ]
        coords.append(coord_tuple)
    return coords

    # Cool alternative I found later:
    # x1,y1,x2,y2 = [[int(x) for x in re.findall('\d+', line)] for line in fileinput.input()]
    # coord_tuple = [[x1,y1],[x2,y2]]
    
def select_lines(coords, diagonal=False):
    filtered_coords = []
    for line in coords:
        (x1,y1),(x2,y2) = line[0],line[1]
        if diagonal:
            if abs(x1-x2) == abs(y1-y2):
                filtered_coords.append(line)
        else:
            if (x1 == x2) or (y1==y2):
                filtered_coords.append(line)
    return filtered_coords

def expand_axis(line, axis=0):
    x1,x2 = line[0][axis], line[1][axis]
    if x1 > x2:
        return [i for i in range(x1,x2-1,-1)]
    return [i for i in range(x1,x2+1)]

def expand_coords(line, diagonal=False):
    xaxis = expand_axis(line, axis=0)
    yaxis = expand_axis(line, axis=1) 
    if diagonal:
        return list(zip(xaxis,yaxis))
    return list(product(xaxis,yaxis))

if __name__ == "__main__":
    filename="../data/day05_input.txt"

    coords = load_file(filename)
    fcoords = select_lines(coords)
    print("Horizontals+Verticals: %d -> %d" % (len(coords), len(fcoords)))
    coord_freq=defaultdict(int)
    for line in fcoords:
        for c in expand_coords(line):
            coord_freq[c]+=1
    n = 0 
    for k,v in coord_freq.items():
        if v >= 2:
            n+=1
    print("Problem 1 - Number: %d" % (n))

    ## --- Problem 2
    diagonals = select_lines(coords, diagonal=True)
    print("Diagonals: %d -> %d" % (len(coords), len(diagonals)))
    for line in diagonals:
        for c in expand_coords(line, diagonal=True):
            coord_freq[c]+=1
    n = 0
    for k,v in coord_freq.items():
        if v >= 2:
            n+=1
    print("Problem 2 - Number: %d" % (n))