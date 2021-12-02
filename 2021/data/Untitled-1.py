fh = open('day01_input.txt', 'r') # this opens a file and returns a filehandle

mylist = list()
for line in fh:
    modified_line = int(line.rstrip())
    mylist.append(modified_line)

print(len(mylist))