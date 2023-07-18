field = [line.strip() for line in open('input.txt').readlines()]
grid = {(x, y): c for y, l in enumerate(field)
                  for x, c in enumerate(l)}
#north, south, west, east
thinkOrder = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#will contain data in the form (target): (contestedStatus, ?from)
proposals = {}

def think(direction, x, y):
    dirX, dirY = direction
    checkX = [x-1, x, x+1]
    checkY = [y-1, y, y+1]
    #north or south
    if dirY != 0:
        #for each of the three points that need checking
        for value in checkX:
            #if it's not in the grid, no point in even checking it's open (also index error)
            if (value, y+dirY) not in grid:
                continue
            #if spot is blocked, give up on movement 
            if grid[(value, y+dirY)] != '.':
                return False
        #if someone else wants to move here, nobody will move here
        if (x, y+dirY) in proposals:
            proposals.update({(x, y+dirY): False})
            return True
        #if nobody else has tried to move here yet, try to move here
        #or
        #if all three points that need checking are not in grid
        proposals.update({(x, y+dirY): (True, (x, y))})
        return True
    #east or west
    else:
        for value in checkY:
            if (x+dirX, value) not in grid:
                continue
            if grid[(x+dirX, value)] != '.':
                return False
        if (x+dirX, y) in proposals:
            proposals.update({(x+dirX, y): False})
            return True
        proposals.update({(x+dirX, y): (True, (x, y))})
        return True

for _ in range(10):
    for location in grid:
        if grid[location] == '#':
            x, y = location
            surrounding = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1)]
            clear = 0
            for spot in surrounding:
                if spot not in grid or grid[spot] == '.':
                    clear += 1
            if len(surrounding) <= clear:
                continue
            for direction in thinkOrder:
                if think(direction, x, y):
                    break
    for target in proposals:
        if proposals[target]:
            grid.update({target: '#'})
            grid.update({proposals[target][1]: '.'})
    thinkOrder.append(thinkOrder.pop(0))
    proposals.clear()

minX = minY = 100
maxX = maxY = count = 0
for location in grid:
    if grid[location] == '#':
        count += 1
        x, y = location
        if x > maxX:
            maxX = x
        if x < minX:
            minX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
print(minX, maxX, minY, maxY, count)
ans = (maxX-minX+1)*(maxY-minY+1) - count
print(ans)
#print(proposals)
