# https://adventofcode.com/2021/day/1
count = 0
previous_measurement = None
for measurement in open('../data/day01_input.txt', 'r'):
    measurement = int(measurement.rstrip())
    if previous_measurement is not None:
        diff = measurement - previous_measurement
        if diff > 0:
            count += 1
    previous_measurement = measurement
print(count)