import math

# Part 1

def SpiralMemory(data):
    distance = 0

    root = int(math.ceil(math.sqrt(data)))

    if(root % 2 == 0):
        root += 1

    distance_from_corner = math.pow(root, 2) - data
    steps = distance_from_corner % (root-1)

    if(steps > root/2):
        steps = abs((root/2) - steps + (root/2))

    distance = (root-1) - steps

    return distance