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
field = np.zeros((1000, 7), dtype = int)
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
                if not all(-1 < x < y for x, y, in zip((coords[0] + i, coords[1] + j), (1000, 7))) or field[coords[0] + i, coords[1] + j] == 1:
                    blocked = True
                    break
    return blocked

def filledLine(y):
    filled = True
    for i in range(len(field[y])):
        if (field[y][i] == 0):
            filled = False
            break
    return filled

def downshift(subarray):
    field.fill(0)
    for i, row in enumerate(subarray):
        field[len(field)-len(subarray)+i] = row

#part2
gustIndex = 0
rockIndex = 0
past = {}
step = 0
totalHeight = 0
highestY = len(field)
patternFound = False

while not patternFound:
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
            if spawn[0] < highestY:
                highestY = spawn[0]
            if rockIndex >= len(rocks) - 1:
                rockIndex = 0
            else:
                rockIndex += 1
            for i in range(4):
                if (spawn[0] + i < 1000 and filledLine(spawn[0] + i)):
                    print(spawn[0] + i, step)
                    remainingRocks = []
                    for lineIndex in range(highestY, spawn[0] + i):
                        remainingRocks.append(list(field[lineIndex]))
                    downshift(remainingRocks)
                    # for p in range(990, 1000):
                    #     print(field[p])
                    stringRocks = ""
                    for line in remainingRocks:
                        for element in line:
                            stringRocks += str(element)
                    totalHeight += 1000-(spawn[0]+i)
                    highestY += 1000-(spawn[0]+i)
                    pastKey = (stringRocks, gustIndex, rockIndex)
                    if pastKey in past:
                        pastStep, pastHeight = past[pastKey]
                        stepDiff = step - pastStep
                        heightDiff = totalHeight + (1000-highestY) - pastHeight
                        patternFound = True
                        break
                    else:
                        past[pastKey] = (step, 1000-highestY + totalHeight)
                    break
        else:
            spawn = (spawn[0] + 1, spawn[1])
    step += 1

possibleRepeats = (1000000000000 - (pastStep + 1)) // stepDiff
totalHeight = pastHeight + (possibleRepeats * heightDiff) - (1000-highestY)
curr_step = pastStep + 1 + (possibleRepeats * stepDiff)

for step in range(curr_step, 1000000000000):
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
            if spawn[0] < highestY:
                highestY = spawn[0]
            if rockIndex >= len(rocks) - 1:
                rockIndex = 0
            else:
                rockIndex += 1
            for i in range(4):
                if (spawn[0] + i < 1000 and filledLine(spawn[0] + i)):
                    remainingRocks = []
                    
                    for lineIndex in range(highestY, spawn[0] + i):
                        remainingRocks.append(list(field[lineIndex]))
                    downshift(remainingRocks)
                    totalHeight += 1000-(spawn[0]+i)
                    highestY += 1000-(spawn[0]+i)
                    break
        else:
            spawn = (spawn[0] + 1, spawn[1])


print(totalHeight + 1000-highestY)
#past 1: 50146000000016427 *dunno what i did here, maybe forgot range(stuff)
#past 2: 2611000000000374 *forgot a parenthesis, messed up math
#past 3: 1554166666665 *forgot a +1 to step
#past 4: 1554166666664 *adjusted downshift to not include filled line
#past 5: 1554166666723 *wait i'm dumb undo that last change
#past 6: 1541449275953 *fixed downshift for real this time
#past 7: 1541449275746 *fixed downshift for both parts of code, not just one
#past 8: 1541449275365 *fixed everything for both parts of code

#real answer: 1541449275365