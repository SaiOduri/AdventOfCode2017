def Trampoline_Maze(f):
    fp = open(f, 'r')
    temp_list = []
    for line in fp:
        temp_list.append(int(line))
    x = temp_list[:]
    print("Part 1: " + str(Part1(temp_list)))
    print("Part 2: " + str(Part2(x)))
    
def Part1(maze):
    current_pos = 0
    steps = 0
    while(current_pos < len(maze)):
        jumps = maze[current_pos]
        maze[current_pos] = maze[current_pos] + 1
        current_pos = current_pos + jumps
        steps += 1
    return steps

def Part2(maze):
    current_pos = 0
    steps = 0
    while(current_pos < len(maze)):
        jump = current_pos + maze[current_pos]
        if(maze[current_pos] >= 3):
            maze[current_pos] += -1
        else:
            maze[current_pos] +=  1
        current_pos = jump
        steps += 1
    return steps