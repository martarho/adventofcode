def read_files(f):
    data = []
    for line in open(f, "r"):
        data.append(line.rstrip())
    return data
