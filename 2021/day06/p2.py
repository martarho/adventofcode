fh = open("../data/day06_input.txt", 'r')
fish = [int(i) for i in fh.readline().rstrip().split(",")]

# vector to represent fish ages instead
# of a list of fish
fish_cycle = [0] * 9
for f in fish:
    fish_cycle[f] += 1
print(fish_cycle)

# iterate the vector of fish per age 
# instead - way smaller!
for day in range(256):
    newfish = fish_cycle[0] # == parents and also new fish
    for c in range(1,len(fish_cycle)):
        fish_cycle[c-1] = fish_cycle[c]
    fish_cycle[6] += newfish
    fish_cycle[8] = newfish #it's actually the parents
print(fish_cycle)
print(sum(fish_cycle))
