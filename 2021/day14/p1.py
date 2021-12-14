from collections import Counter

def load_file(filename="../data/day14_test.txt"):
    template,insertions=None,{}
    for line in open(filename,"r").readlines():
        if '->' in line:
            k,v = line.rstrip().split(" -> ")
            insertions[k] = v
        elif line.rstrip()!="":
            template = line.rstrip()
    return list(template),insertions

def sliding_window(s,w=2):
    for i in range(len(s)-w+1):
        yield s[i:i+w]

def insertion_round(template,insertions):
    new_template = [template[0]]
    for pair in sliding_window(template):
        new_template.extend([insertions[''.join(pair)],pair[-1]])
    return new_template

# part 1
template,insertions = load_file("../data/day14_input.txt")
for i in range(10):
    template = insertion_round(template, insertions)

freq = Counter(template).most_common()
print(freq)
print(freq[0][1]-freq[-1][1])

# part 2
template,insertions = load_file("../data/day14_test.txt")
for i in range(40):
    template = insertion_round(template, insertions)

freq = Counter(template).most_common()
print(freq)
print(freq[0][1]-freq[-1][1])