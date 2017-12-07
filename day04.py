def passphrase(f):
    fp = open(f)
    sum = 0
    for line in fp:
        temp_list = line.split()
        if(not(passphrase_helper(temp_list))):
            sum += 1
    return sum

def passphrase_helper(seq):
    return any(seq.count(x) > 1 for x in seq)

def passphrase2(f):
    fp = open(f)
    sum = 0
    for line in fp:
        temp_list = line.split()
        if(not(passphrase2_helper(temp_list))):
            sum += 1
    return sum

def passphrase2_helper(lst):
    new_lst = []
    retv = False
    for element in lst:
        new_lst.append(sorted(element))
    for i in range(len(new_lst)):
        if(new_lst[i] in new_lst[0:i]+new_lst[i+1:]):
            retv = True
    return retv

#input_ = "day04input.txt"
#print(passphrase(input_))
#print(passphrase2(input_))