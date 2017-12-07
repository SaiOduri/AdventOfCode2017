# PART 1
def checksum(f):
    fp = open(f)
    difference = 0
    for line in fp:
        temp_list = line.split()
        temp_list = map(int, temp_list)
        difference += max(temp_list) - min(temp_list)
    return difference

# PART 2
def checksum2(f):
    fp = open(f)
    sum = 0
    for line in fp:
        temp_list = line.split()
        temp_list = map(int, temp_list)
        for i in range(len(temp_list)):
            for j in range(len(temp_list)):
                if(temp_list[i] % temp_list[j] == 0 and i != j):
                    sum += temp_list[i]/temp_list[j]
                    break
    return sum