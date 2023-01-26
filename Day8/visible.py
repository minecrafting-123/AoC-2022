#coords are in the format [y, x], 0 indexed
coords = []
numVisible = 0

with open("input.txt") as reader:
    for line in reader:
        x = []
        for char in line:
            x.append(char)
        coords.append(x)

def beegCheck(x, y):
    height = coords[y][x]
    checksFailed = 0
    if (x == 0 or x == len(coords) or y == 0 or y == len(coords)):
        return True
    for i in range(0, x, 1):
        if (coords[y][i] >= height):
            checksFailed += 1
            break
    for j in range(x+1, len(coords), 1):
        if (coords[y][j] >= height):
            checksFailed += 1
            break
    for k in range(0, y, 1):
        if (coords[k][x] >= height):
            checksFailed += 1
            break
    for l in range(y+1, len(coords), 1):
        if (coords[l][x] >= height):
            checksFailed += 1
            break
    if (checksFailed == 4):
        return False
    return True


#goes through all values and checks for visibility
for i in range(len(coords)):
    for k in range(len(coords)):
        if (beegCheck(i, k)):
            numVisible += 1

print(numVisible)