from collections import Counter

def load_measurements():
    measurements = []
    for line in open('../data/day03_input.txt', 'r'):
        binary_string = line.rstrip()
        measurements.append(binary_string)
    return measurements

def l2tl(string_list):
    l = []
    for i in string_list:
        l.append(list(i))
    transposed_l = list(map(list, zip(*l)))
    return transposed_l

def remove_strings(string_list, idx, keeper):
    to_keep = []
    for s in string_list:
        if s[idx] == str(keeper):
            to_keep.append(s)
    return to_keep

def get_ratio_string(string_list, freq_index=0, max_freq=2):
    list_of_ints = list(range(max_freq))[::-1]
    for idx in range(index_length):
        transposed = l2tl(string_list)
        c = Counter(transposed[idx])
        freq = c.most_common(max_freq)

        if freq[0][1] == freq[1][1]:
            keeper = list_of_ints[freq_index]
        else:
            keeper = freq[freq_index][0]
        string_list = remove_strings(string_list, idx, keeper)
        if len(string_list) == 1:
            return string_list
    return string_list

measurements = load_measurements()
index_length = len(measurements[0])
o2 = get_ratio_string(measurements, 0, 2)
co2 = get_ratio_string(measurements, 1, 2)

o2_value = int(''.join(o2),2)
co2_value = int(''.join(co2),2)

print("o2: %d; co2: %d" % (o2_value, co2_value))
print("life support value: %d" % (o2_value*co2_value))