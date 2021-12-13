import numpy as np 
import re
from copy import deepcopy

def load_file(filename="../data/day13_test.txt"):
    fh = open(filename,"r")
    folds = []
    coords = []
    for line in fh.readlines():
        if line.startswith("fold"):
            fold = line.rstrip().split(" ")[2]
            folds.append(fold.split("="))
        elif ',' in line:
            c = [int(x) for x in line.rstrip().split(",")]
            coords.append(tuple(c))
        else:
            pass
    return coords,folds

def fold(matrix, pos):
    axis,fold = pos[0],int(pos[1])
    if axis == "x":
        left_fold = matrix[:,0:fold]
        right_fold = np.flip(matrix[:,fold+1:],axis=1)
        folded = deepcopy(left_fold)
        stt = right_fold.shape[1] - fold
        folded[:,stt:] += right_fold
        folded[folded>1] = 1
    elif axis == "y":
        upper_fold = matrix[:fold,]
        lower_fold = np.flip(matrix[fold+1:,],axis=0)
        folded = deepcopy(upper_fold)
        stt = lower_fold.shape[0] - fold
        folded[-stt:,] += lower_fold
        folded[folded>1] = 1
    return folded

def print_character(mtx):
    ll = mtx.tolist()
    for subl in ll:
        subs = ''.join(['. ' if x == 0 else '# ' for x in subl])
        print(subs)

coords,folds = load_file("../data/day13_input.txt")
#coords,folds = load_file()

maxx=max([x[0] for x in coords])
maxy=max([x[1] for x in coords])
matrix = np.zeros((maxy+1,maxx+1))

for x,y in coords:
    matrix[y,x] = 1

# Part 1
folded = fold(matrix,folds[0])
print(np.count_nonzero(folded>0))

# Part 2
folded_matrix = deepcopy(matrix)
for f in folds:
    folded_matrix = fold(folded_matrix,f)
print_character(folded_matrix)
