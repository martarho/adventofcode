from itertools import permutations

def parse_input(l):
    i,o = l.split(" | ")
    return i.split(" "),o.split(" ")

fh = open("../data/day08_input.txt", 'r')
data = []
for l in fh.readlines():
    data.append(parse_input(l.rstrip()))

def translate(s,d):
    return ''.join(sorted([d[x] for x in list(s)]))

def is_permutation(s,p,d, MC):
    """ 
    Translate all signal codes with the permutation
    if they all match the master signal list, then True
    """
    for i in s:
        it = translate(i, d)
        if it not in MC:
            return False
    return True

MASTERCODE = ["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]
d8 = list("abcdefg")
perms = [x for x in permutations(d8)]
cumsumvalue = 0
for l in data:
    signal, out = l
    value = None
    for p in perms:
        d = dict(zip(p,d8))
        if is_permutation(signal, p,d, MASTERCODE):
            translated = [translate(o,d) for o in out]
            value = int(
                ''.join(
                    list(
                        map(str,[
                            MASTERCODE.index(t) for t in translated
                            ]
                        )
                    )
                )
            )
            cumsumvalue+=value
print(cumsumvalue)