import numpy as np 
from itertools import product

def load_data(filename="../data/day11_input.txt"):
    fh = open(filename,"r")
    matrix = []
    for l in fh.readlines():
        matrix.append([int(i) for i in list(l.rstrip())])
    return np.array(matrix).astype('float')

def flash_neighbours(mtx):
    original_flashes = np.array(list(zip(*np.where(mtx > 9))))
    offsets = np.array([c for c in product([-1,0,1],repeat=2) if c != (0,0)])
    for xy in original_flashes:
        for x,y in xy+offsets:
            if x < mtx.shape[0] and y < mtx.shape[0] and x>-1 and y > -1:
                mtx[x,y] += 1 
    for x,y in original_flashes:
        mtx[x,y] = np.nan # remove original
    mtx[mtx > 9] = 10

    return mtx

matrix = load_data()
total_flashes = 0
for step in range(100):
    matrix += 1
    new_flashes = np.count_nonzero(matrix>9)
    total_flashes += new_flashes
    while new_flashes > 0:
        matrix = flash_neighbours(matrix)
        new_flashes = np.count_nonzero(matrix>9)
        total_flashes += new_flashes
    matrix[np.isnan(matrix)] = 0

# part 1
print(total_flashes)

matrix = load_data()
nsteps = 0
while True:
    nsteps += 1
    matrix += 1
    new_flashes = np.count_nonzero(matrix>9)
    while new_flashes > 0:
        matrix = flash_neighbours(matrix)
        new_flashes = np.count_nonzero(matrix>9)
    matrix[np.isnan(matrix)] = 0
    if np.all(matrix == 0):
        # part 2
        print(nsteps)
        break
        