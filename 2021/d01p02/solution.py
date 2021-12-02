# https://adventofcode.com/2021/day/1
measurements = []
window_size = 3
count = 0

with open('../data/day01_input.txt', 'r') as f:
    measurements = [int(measurement.rstrip())for measurement in f]

aggregated_measurements = []
for i in range(len(measurements)-window_size +1):
    aggregated_measurements.append(sum(measurements[i:i+window_size]))


for i in range(len(aggregated_measurements)-1):
    diff = aggregated_measurements[i+1] - aggregated_measurements[i]
    if diff > 0:
        count += 1

print(count)