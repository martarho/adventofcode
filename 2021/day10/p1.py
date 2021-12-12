from statistics import median

fh = open("../data/day10_input.txt", 'r')
code = []
for l in fh.readlines():
    code.append(list(l.rstrip()))

chr_map = {'(':')','<':'>','{':'}','[':']'}
scoring_map = {')':3,']':57,'}':1197,'>':25137}
scoring_map2 = {')':1,']':2,'}':3,'>':4}

def check_line(l):
    ll = []
    for c in l:
        if c in chr_map:
            ll.append(c)
        else:
            if len(ll) == 0:
                return scoring_map[c] 
            last_open = ll.pop()
            if c != chr_map[last_open]:
                return scoring_map[c]
    return 0

def complete_line(l):
    ll = []
    for c in l:
        if c in chr_map:
            ll.append(c)
        else:
            ll.pop()
    rev = [chr_map[c] for c in reversed(ll)]
    return rev

part1_score = 0
incomplete_lines = []
for line in code:
    ls = check_line(line)
    part1_score+=ls
    if ls == 0:
        score = 0
        comp = complete_line(line)
        for c in comp:
            score = (score * 5) + scoring_map2[c]
        incomplete_lines.append(score)


print(part1_score)
print(median(incomplete_lines))