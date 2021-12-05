from collections import Counter

def load_measurements():
    measurements = []
    for line in open('../data/day03_input.txt', 'r'):
        list_of_ints = [int(i) for i in list(line.rstrip())]
        measurements.append(list_of_ints)
    return measurements

measurements = load_measurements()
transposed_measurements = list(map(list, zip(*measurements)))

gamma = []
epsilon = []
for idx in transposed_measurements:
    c = Counter(idx)
    freq = c.most_common(2)
    gamma.append(str(freq[0][0]))
    epsilon.append(str(freq[1][0]))

gamma_number = int(''.join(gamma),2)
epsilon_number = int(''.join(epsilon),2)

print(gamma_number*epsilon_number)