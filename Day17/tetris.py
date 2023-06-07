import numpy as np

gusts = list()
with open("input.txt", 'r') as reader:
    temp = [line.strip() for line in reader.readlines()]
    for char in temp[0]:
        if (char == "<"):
            gusts.append(-1)
        elif (char == ">"):
            gusts.append(1)
#Loop through these for da rocks
rocks = [
    [[1, 1, 1, 1]],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]
field = np.zeros((10000, 7), dtype = int)
highestY = len(field)
#spawns a rock with shape 'rock' with top left corner at tuple 'coords' (y, x)
def renderRock(coords, rock):
    for i, row in enumerate(rock):
        for j, val in enumerate(row):
            if (val == 1):
                field[coords[0] + i, coords[1] + j] = 1
#checks if coords are blocked for a rock
def check(coords, rock):
    #print(coords)
    blocked = False
    for i, row in enumerate(rock):
        for j, val in enumerate(row):
            if (val == 1):
                if not all(-1 < x < y for x, y, in zip((coords[0] + i, coords[1] + j), (10000, 7))) or field[coords[0] + i, coords[1] + j] == 1:
                    blocked = True
                    break
    return blocked
#part1
gustIndex = 0
rockIndex = 0
for i in range(2022):
    #print(gustIndex)
    #print(rockIndex)
    spawn = (highestY - 3 - len(rocks[rockIndex]), 2)
    atRest = False
    while(not atRest):
        #print(spawn)
        #print(gusts[gustIndex])
        if (not check((spawn[0], spawn[1] + gusts[gustIndex]), rocks[rockIndex])):
            spawn = (spawn[0], spawn[1] + gusts[gustIndex])
        if (gustIndex >= len(gusts)-1):
            gustIndex = 0
        else:
            gustIndex += 1
        if check((spawn[0] + 1, spawn[1]), rocks[rockIndex]):
            renderRock(spawn, rocks[rockIndex])
            # for i in range(9990, 10000):
            #     print(field[i])
            atRest = True
        else:
            spawn = (spawn[0] + 1, spawn[1])
        #print(atRest)
    if spawn[0] < highestY:
        highestY = spawn[0]
    if rockIndex >= len(rocks) - 1:
        rockIndex = 0
    else:
        rockIndex += 1
print(10000-highestY)

def filledLine(y):
    filled = True
    for i in range(len(field[y])):
        if (field[y][i] == 0):
            filled = False
            break
    return filled

def downshift(subarray):
    field.fill(0)
    
#part2
gustIndex = 0
rockIndex = 0
while True:
    spawn = (highestY - 3 - len(rocks[rockIndex]), 2)
    atRest = False
    while(not atRest):
        if (not check((spawn[0], spawn[1] + gusts[gustIndex]), rocks[rockIndex])):
            spawn = (spawn[0], spawn[1] + gusts[gustIndex])
        if (gustIndex >= len(gusts)-1):
            gustIndex = 0
        else:
            gustIndex += 1
        if check((spawn[0] + 1, spawn[1]), rocks[rockIndex]):
            renderRock(spawn, rocks[rockIndex])
            atRest = True
        else:
            spawn = (spawn[0] + 1, spawn[1])
    if spawn[0] < highestY:
        highestY = spawn[0]
    if rockIndex >= len(rocks) - 1:
        rockIndex = 0
    else:
        rockIndex += 1