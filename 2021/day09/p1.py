import numpy as np
from scipy.ndimage.filters import minimum_filter
from scipy.ndimage import label
from scipy.ndimage.morphology import generate_binary_structure

def load_data(filename="../data/day09_input.txt"):
    fh = open(filename, 'r')
    data = []
    for l in fh.readlines():
        l = l.rstrip()
        data.append([int(i) for i in list(l)])

    return np.array(data)


data = load_data()

# Part 1
minimums = minimum_filter(data, 3)
result = data[data == minimums]
print(np.sum(result+1))

# Part 2
basins, n_basins = label(data !=9)
basin_sizes = np.bincount(basins[basins!=0].flatten())
biggest_basins = -np.sort(-basin_sizes)[0:3]
result = np.product(biggest_basins)
print(result)
