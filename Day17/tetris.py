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
print(spawn)
renderRock(spawn, rocks[4])
print(field)