from statistics import median, mean
fh = open("../data/day07_input.txt", 'r')
xs = [int(i) for i in fh.readline().rstrip().split(",")]

median_point = median(xs)
fuel = sum([abs(x-median_point) for x in xs])
print(int(fuel))

# -- part 2
def calculate_fuel(n,xs):
    total_fuel = 0
    for x in xs:
        d = abs(x-n)
        total_fuel += sum(list(range(d+1)))            
    return total_fuel

min_fuel = None
for n in range(min(xs),max(xs)):
    fuel = calculate_fuel(n, xs)
    if (min_fuel == None) or (min_fuel>fuel):
        min_fuel = fuel
print(min_fuel)

