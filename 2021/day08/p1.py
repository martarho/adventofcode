
def parse_input(l):
    i,o = l.split(" | ")
    return i.split(" "),o.split(" ")

fh = open("../data/day08_input.txt", 'r')
data = []
for l in fh.readlines():
    data.append(parse_input(l.rstrip()))

digit_segments = {
    "1":2,
    "4":4,
    "7":3,
    "8":7
}
print(data)
digit_segments = [2,3,4,7]
c = 0
for s,o in data:
	for d in o:
		if len(d) in digit_segments:
			c += 1
print(c)