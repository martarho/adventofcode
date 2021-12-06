fh = open("../data/day06_input.txt", 'r')
fish = [int(i) for i in fh.readline().rstrip().split(",")]

def calculate_fish(n):
    for day in range(n):
        newfish = []
        for i,f in enumerate(fish):
            if f == 0:
                newfish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        fish.extend(newfish)
    return fish

print(len(calculate_fish(80)))
# takes too long -- print(len(calculate_fish(256))) 