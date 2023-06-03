import numpy as np

with open("input.txt", 'r') as reader:
    gusts = [line.strip() for line in reader.readlines()]
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
highestY = len(field) - 1
# (y, x)
spawn = (highestY - 3, 2)
# spawns a rock with shape 'rock' with top left corner at tuple 'coords' (y, x)
def renderRock(coords, rock):
    for i, row in enumerate(rock):
        for j, val in enumerate(row):
            field[coords[0] + i, coords[1] + j] = 1
def fall(coords, rock, direction):
    blocked = False
    movedCoords = coords
    for i, row in enumerate(rock):
        for j, val in enumerate(row):
            #If it goes out of bounds on Y axis
            if (coords[0] + len(rock) - i > len(field) - 1):
                blocked = True
                break
            #If it goes out of bounds on X axis
            if (coords[1] + len(row) - j < 0 or coords[1] + len(row) - j >= 7):
                blocked = True
                break
            #If there is another rock in the way
            if (field[coords[0] + len(rock) - i, coords[1] + len(row) - j] == 1):
                blocked = True
                break
    #Gust blows
    if (coords[1] + direction >= 0 and coords[1] + direction < 7):
        gusted = True
        for i, row in enumerate(rock):
            if (row.find(1) != -1):
                if()
        movedCoords = tuple(coords[0], coords[1] - 1)
    if (blocked):
        renderRock(coords, rock)
    else:
        fall((coords[0] + 1, coords[1] + 1), rock)