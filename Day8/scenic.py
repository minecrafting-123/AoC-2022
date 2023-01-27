#coords are in the format [y, x], 0 indexed
coords = []

with open("input.txt") as reader:
    for line in reader:
        x = []
        for char in line:
            x.append(char)
        coords.append(x)

def beegCheck(x, y):
    height = coords[y][x]
    a = 0
    b = 0
    c = 0
    d = 0
    if (x == 0 or x == len(coords) or y == 0 or y == len(coords)):
        return 0
    for i in range(x-1, -1, -1):
        a += 1
        if (coords[y][i] >= height):
            break
    for j in range(x+1, len(coords), 1):
        b += 1
        if (coords[y][j] >= height):
            break
    for k in range(y-1, -1, -1):
        c += 1
        if (coords[k][x] >= height):
            break
    for l in range(y+1, len(coords), 1):
        d += 1
        if (coords[l][x] >= height):
            break
    score = a*b*c*d
    return score


#goes through all values and checks for visibility
beegScore = 0
for i in range(len(coords)):
    for k in range(len(coords)):
        if (beegCheck(i, k) > beegScore):
            beegScore = beegCheck(i, k)

print(beegScore)