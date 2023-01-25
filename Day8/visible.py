#coords are in the format [y, x], 0 indexed
coords = []
numVisible = 0

open ("input.txt") as reader:
    for line in reader:
        x = []
        for char in line:
            x.append(char)
        coords.append(x)

def beegCheck(x, y):
    height = coords[y][x]
    if (x == 0 or x == coords[0].len() or y == 0 or y == coords.len()):
        return true
    for i in range(x, 0, -1):
        if (coords[y][i] >= height):

#goes through all values and checks for visibility
for i in range(coords.len()):
    for k in range(coords[0].len()):
        if (beegCheck(i, k)):
            numVisible += 1

print(numVisible)