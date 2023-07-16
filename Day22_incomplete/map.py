
import re

#clockwise, starting from up
directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

with open('input.txt', 'r') as reader:
    input = [line.replace("\n", "") for line in reader.readlines()]
    place = input[:input.index("")]
    steps = input[-1]
grid = {(x, y): c for x, l in enumerate(place)
                for y, c in enumerate(l) if c in '.#'}
#Start with nums
# nums = [int(num) for num in re.findall("([0-9]+)", steps)]
# dirs = re.findall("([A-Z])", steps)
moves = re.findall(r'\d+|[RL]', steps)

#REMEMBER THAT YOU ARE USING (y,x)
for point in grid:
    if grid[point] == '.':
        pos = point
    break
print(pos)
facing = 1

def add(i, j):
    return  tuple(map(sum, zip(i, j)))

def loop(target):
    global facing
    if facing == 0:
        for i in range(len(grid)-1, 0, -1):
            if grid[(i, target[1])] == "." or grid[(i, target[1])] == "#":
                new = (i, target[1])
                break
    elif facing == 1:
        for i in range(0, len(grid[0])-1, 1):
            if grid[(target[0], i)] == "." or grid[(target[0], i)] == "#":
                new = (target[0], i)
                break
    elif facing == 2:
        for i in range(0, len(grid)-1, 1):
            if grid[(i, target[1])] == "." or grid[(i, target[1])] == "#":
                new = (i, target[1])
                break
    elif facing == 3:
        for i in range(len(grid[0])-1, 0, -1):
            if grid[(target[0], i)] == "." or grid[(target[0], i)] == "#":
                new = (target[0], i)
                break
    print(new)
    return new

def loop2(target):
    global facing
    #print(target)
    if facing == 0:
        if target[1] < 50:
            new = (50+target[1], 50)
            facing = 1
        elif target[1] < 100:
            new = (100+target[1], 0)
            facing = 1
        else:
            new = (199, target[1]-100)
    elif facing == 1:
        #flip!
        if target[0] < 50:
            new = (149-target[0], 99)
            facing = 3
        elif target[0] < 100:
            new = (49, target[0]+50)
            facing = 0
        #flip!
        elif target[0] < 150:
            new = (149-target[0], 149)
            facing = 3
        else:
            new = (149, target[0]-100)
            facing = 0
    elif facing == 2:
        if target[1] < 50:
            new = (0, 100+target[1])
        elif target[1] < 100:
            new = (target[1]+100, 49)
            facing = 3
        else:
            new = (target[1]-50, 99)
            facing = 3
    elif facing == 3:
        #flip!
        if target[0] < 50:
            new = (149-target[0], 0)
            facing = 1
        elif target[0] < 100:
            new = (100, target[0]-50)
            facing = 2
        #flip!
        elif target[0] < 150:
            new = (149-target[0], 50)
            facing = 1
        else: 
            new = (0, target[0]-100)
            facing = 2
    return new
def adjust():
    global facing
    if facing < 0:
        facing += 4
    facing %= 4

def move(movement):
    global pos, facing
    #print(pos, facing)
    print(movement)
    for i in range(int(movement)):
        target = add(pos, directions[facing])
        print(grid[target])
        try:
            grid[target]
        except:
            print("Except here!", target)
            target = loop(target)
        if grid[target] == " " or grid[target] == "":
            print("Loop here!", target)
            target = loop(target)
        if grid[target] == "#":
            return
        pos = target

for thing in re.findall(r'\d+|[RL]', steps):
    match thing:
        case 'L': 
            facing += 1
            adjust()
        case 'R':
            facing -= 1
            adjust()
        case _:
            for _ in range(int(thing)):
                target = add(pos, directions[facing])
                if target not in grid: target = loop2(target)
                if grid[target] == '.': pos = target
    print(pos, facing)
ans = (pos[0]+1)*1000 + (pos[1]+1)*4 + ((facing+3)%4)
print(ans)

#part2 try1 11394 too low
#part2 try2 133159 too high
#part2 try3 36412 too low