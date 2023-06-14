with open("input.txt", "r") as reader:
    coords = [line.strip().split(',') for line in reader.readlines()]

#pretty sure dimensions are 20x20x20 but I'll write this to make the code generic
#good thing I wrote this, it was 21x21x21 if I assumed 20x20x20 it would have ruined my code + taken way too long for me to realize my dumb
xMax = 0
yMax = 0
zMax = 0

for coord in coords:
    for i in range(len(coord)):
        coord[i] = int(coord[i])
    if coord[0] > xMax:
        xMax = coord[0]
    if coord[1] > yMax:
        yMax = coord[1]
    if coord[2] > zMax:
        zMax = coord[2]

# acts as a straight up 3D model - prob not the most elegant method but it's the first thing I thought of
# yeah this method kinda sucks but i still feel like it should function dunno why it borking
model = [[[0 for width in range(zMax+1)] for col in range(yMax+1)] for row in range(xMax+1)]

#counts adjacent cubes
def comp(x, y, z):
    adj = 0
    for i in range(-1, 2, 2):
        if (0 <= x+i <= xMax and model[x+i][y][z] == 1):
            adj += 1
        if (0 <= y+i <= yMax and model[x][y+i][z] == 1):
            adj += 1
        if (0 <= z+i <= zMax and model[x][y][z+i] == 1):
            adj += 1
    return adj

#part 1
SA = 0
for coord in coords:
    x, y, z = coord
    model[x][y][z] = 1
    SA += 6 - comp(x, y, z)*2

print(SA)

#past 1: 4446 *adjusted bounds in comp
#past 2: 4404 *see above but i actually used brain hopefully
#past 3: 4328 (too low or smth? idk why is this wrong - there are no duplicate coords in case that was possible)
#past 4: 4332 GOT IT LETS GOOOOO

# THERE WAS A POINT WITH 0 AS A COORD - NEVER ASSUMING ANYTHING EVER AGAIN AHHHHH

#part 2
#used below to make sure I don't stop adding early


#TODO
#somehow determine if something is encompassed by drop
#first thought: loop in all four directions and detect if 4 barriers are found - but what if there's a curved bit or whatever - if reaches edge of array without barrier
#consider curved bit later if straight up comps don't work
#mark "bad" spaces with a -1 
# NEW IDEA SPREAD A VALUE THAT REPS "unbound" - nope, too much recursion apparently hmm

directions = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}
#what this code does is fill air pockets that are completely surrounded with -1
#print(xMax, yMax, zMax)
def try1():
    maxMax = max(xMax, yMax, zMax)

    def improvedComp(xOG, yOG, zOG):
        testables = []
        for direction in directions:
            x, y, z = map(lambda i, j: i + j, (xOG, yOG, zOG), direction)
            if 0 <= x <= xMax and 0 <= y <= yMax and 0 <= z <= zMax and model[x][y][z] == 0:
                testables.append((x, y, z))
        return testables
    for coord in coords:

        x, y, z = coords[l]
        print(x, y, z)
        #no point in testing a point if it's surrounded anyways
        if not comp(x, y, z) == 6:
            unbound = False
            for space in improvedComp(x, y, z):
                unbound = False
                print(space)
                for direction in directions:
                    if (unbound):
                        break
                    unbound = False
                #in this case, xMax yMax and zMax are all the same so this isn't necessary, but generic code for the win!
                    for k in range(1, maxMax):
                        xtest, ytest, ztest = map(lambda i, j: i + j * k, space, direction)
                        print(xtest, ytest, ztest)
                        if not (0 <= xtest <= xMax and 0 <= ytest <= yMax and 0 <= ztest <= zMax):
                            print("unbound")
                            unbound = True
                            break
                        if (model[xtest][ytest][ztest] == 1 or model[xtest][ytest][ztest] == -1):
                            print("blocko")
                            break
                #if the air pocket is completely surrounded
                print("fill or not?")
                if not unbound:
                    print("filled")
                    xspace, yspace, zspace = space
                    model[xspace][yspace][zspace] = -1

        #subtracts for each filled air bubble
        for x in range(len(model)):
            for y in range(len(model[x])):
                for z in range(len(model[x][y])):
                    if (model[x][y][z] == -1):
                        SA -= comp(x, y, z)

        print(SA)
        #past 1: 2509 *too low

def try2():
    global SA
    visited = set()

    def BFSish(x, y, z):
        count = 0
        queue = [(x, y, z)]

        while len(queue) > 0:
            next = queue.pop(0)
            count += 1
            if count % 1000 == 0: 
                print(count)
            if next in visited:
                continue
            visited.add(next)
            for direction in directions:
                newx, newy, newz = map(lambda i, j: i + j, next, direction)
                #print(newx, newy, newz)
                if 0 <= newx <= xMax and 0 <= newy <= yMax and 0 <= newz <= zMax and model[newx][newy][newz] == 0:
                    model[newx][newy][newz] = 2
                    queue.append((newx, newy, newz))
    model[0][0][0] = 2
    BFSish(0, 0, 0)
    for x in range(len(model)):
        for y in range(len(model[x])):
            for z in range(len(model[x][y])):
                if (model[x][y][z] == 0):
                    SA -= comp(x, y, z)
    print(SA)

try2()
#WE WIN THESE