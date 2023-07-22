#here's the plan: try to move all 5 possibilities, and add 1 time(t) each move attempt 

field = [line.strip() for line in open('input.txt').readlines()]
grid = {(x, y): c for y, l in enumerate(field)
                  for x, c in enumerate(l) if c != '#'}
#x is [1-120] and y is [0-26]
minX = minY = 100
maxX = maxY = 0
for location in grid:
        x, y = location
        if x > maxX:
            maxX = x
        if x < minX:
            minX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

start = (1, 0)

#(pos, field)
queue = [(start, 0)]

def drift(oldGrid):
    newGrid = {}
    for (x, y) in oldGrid:
        for blizzard in oldGrid[(x, y)]:
            match blizzard:
                case '<':
                    if (x-1, y) not in oldGrid:
                        new = (maxX, y)
                    else: 
                        new = (x-1, y)
                    if new in newGrid and newGrid[new] != '.':
                        newGrid.update({new: newGrid[new]+blizzard})
                    else:
                        newGrid.update({new: ('<')})
                case '>':
                    if (x+1, y) not in oldGrid:
                        new = (minX, y)
                    else: 
                        new = (x+1, y)
                    if new in newGrid and newGrid[new] != '.':
                        newGrid.update({new: newGrid[new]+blizzard})
                    else:
                        newGrid.update({new: ('>')})
                case '^':
                    if (x, y-1) not in oldGrid:
                        new = (x, maxY-1)
                    else: 
                        new = (x, y-1)
                    if new in newGrid and newGrid[new] != '.':
                        newGrid.update({new: newGrid[new]+blizzard})
                    else:
                        newGrid.update({new: ('^')})
                case 'v':
                    if (x, y+1) not in oldGrid:
                        new = (x, minY+1)
                    else: 
                        new = (x, y+1)
                    if new in newGrid and newGrid[new] != '.':
                        newGrid.update({new: newGrid[new]+blizzard})
                    else:
                        newGrid.update({new: ('v')})
        if (x, y) not in newGrid:
            newGrid.update({(x, y): '.'})
    return newGrid
#maxTime = 0
states = {0: grid}
visited = set()
def move(pos, time):
    global visited
    # global maxTime
    # if time > maxTime:
    #     maxTime = time
    #     print(maxTime)
    print(pos, time)
    # if time == 1:
    #     exit()
    x, y = pos
    moves = [(x+1, y), (x, y+1), (x, y), (x-1, y), (x, y-1)]
    if time+1 not in states:
        states.update({time+1: drift(states[time])})
    next = states[time+1]
    for movement in moves:
        if movement in next and next[movement] == '.' and (movement, time) not in visited:
            visited.add((movement, time))
            if movement == (maxX, maxY):
                print("FINAL!!!", time+1)
                exit()
            if pos == movement and pos == start and len(queue) > 0:
                return
            queue.append((movement, time+1))
    
while len(queue) > 0:
    pos, t = queue.pop(0)
    move(pos, t)
