import re
    
with open("input.txt") as reader:
    lines = [line.strip() for line in reader.readlines()]

data = list(map(lambda line : re.findall(r'-?\d+', line), lines))
numData = [list(map(lambda num : int(num), d)) for d in data]

dist = lambda x1, y1, x2, y2 : abs(x1 - x2) + abs(y1 - y2)
part1y = 2000000
nots = 0
minX, minY = 1000000, 1000000
maxX, maxY = 0, 0
for sx, sy, bx, by in numData:
    radius = dist(sx, sy, bx, by)
    if (sx + radius > maxX):
        maxX = sx + radius
    if (sx - radius < minX):
        minX = sx - radius
    if (sy + radius > maxY):
        maxY = sy + radius
    if (sy - radius < minY):
        minY = sy - radius

part1Data = []
for sx, sy, bx, by in numData:
    radius = dist(sx, sy, bx, by)
    if (sy <= part1y and sy + radius >= part1y) or (sy >= part1y and sy - radius <= part1y):
        part1Data.append((sx, sy, bx, by))
for x in range(minX, maxX+1):
    if (x % 100000 == 0):
        print(x)
    for sx, sy, bx, by in part1Data:
        if ((x, part1y) == (bx, by)):
            break
        if (dist(sx, sy, x, part1y) <= dist(sx, sy, bx, by)):
            nots += 1
            break

print(nots)

part2y = 4000000
def inDaRange(px, py):
    for sx, sy, bx, by in numData:
        if (dist(sx, sy, px, py) <= dist(sx, sy, bx, by)):
            return True
    return False
            
def getCoords(sx, sy, r):
    checkThese = []
    for i in range(r + 1):
        #top right
        px, py = sx + i , sy + r - i + 1
        if (py <= part2y and py >= 0 and px >= 0 and px <= part2y):
            checkThese.append((px, py))
        #bottom right
        px, py = sx + r - i + 1, sy - i
        if (py <= part2y and py >= 0 and px >= 0 and px <= part2y):
            checkThese.append((px, py))
        #bottom left
        px, py = sx - i, sy - r + i - 1
        if (py <= part2y and py >= 0 and px >= 0 and px <= part2y):
            checkThese.append((px, py))
        #top left
        px, py = sx - r + i - 1, sy + i
        if (py <= part2y and py >= 0 and px >= 0 and px <= part2y):
            checkThese.append((px, py))
    return checkThese
for sx, sy, bx, by in numData:
    coordFound = False
    check = getCoords(sx, sy, dist(sx, sy, bx, by))
    for point in check:
        if not inDaRange(point[0], point[1]):
            coordFound = True
            print(point[0] * 4000000 + point[1])
            break
    if coordFound:
        break