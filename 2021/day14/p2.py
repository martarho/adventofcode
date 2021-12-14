from collections import Counter,defaultdict

def load_file(filename="../data/day14_test.txt"):
    template,insertions=None,{}
    for line in open(filename,"r").readlines():
        if '->' in line:
            k,v = line.rstrip().split(" -> ")
            insertions[k] = v
        elif line.rstrip()!="":
            template = line.rstrip()
            duplets = defaultdict(int)
            for i in sliding_window(template):
                duplets[i]+=1
    return template,duplets,insertions

def sliding_window(s,w=2):
    for i in range(len(s)-w+1):
        yield ''.join(s[i:i+w])

def insertion_round(duplets,insertions):
    new = defaultdict(int)
    for pair in duplets.keys():
        new[pair[0]+insertions[pair]]+=duplets[pair]
        new[insertions[pair]+pair[1]]+=duplets[pair]
    return new

# part 2
template,duplets,insertions = load_file("../data/day14_input.txt")
for i in range(40):
    duplets = insertion_round(duplets, insertions)

units = defaultdict(int)
for k,v in duplets.items():
    units[k[0]] += v
units[template[-1]]+=1

pairmax = max(units.keys(), key=(lambda k: units[k]))
pairmin = min(units.keys(), key=(lambda k: units[k]))

print(units[pairmax]-units[pairmin])