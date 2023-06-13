with open("input.txt", "r") as reader:
    coords = [line.strip().split(',') for line in reader.readlines()]

#pretty sure dimensions are 20x20x20 but I'll write this to make the code generic
#good thing I wrote this, it was 21x21x21 if I assumed 20x20x20 it would have ruined my code + taken way too long for me to realize my dumb
xMax = 0
yMax = 0
zMax = 0

for coord in coords:
    for i in range(len(coord)):
        coord[i] = int(coord[i]) - 1
    if coord[0] > xMax:
        xMax = coord[0]
    if coord[1] > yMax:
        yMax = coord[1]
    if coord[2] > zMax:
        zMax = coord[2]

# acts as a straight up 3D model - prob not the most elegant method but it's the first thing I thought of
# yeah this method kinda sucks but i still feel like it should function dunno why it borking
# the +1 is to correct the movement i made earlier to index easier
model = [[[0 for width in range(zMax+1)] for col in range(yMax+1)] for row in range(xMax+1)]
# also need to correct bounds
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
SA = 0
for coord in coords:
    x, y, z = coord
    #print(coord)
    model[x][y][z] = 1
    SA += 6 - comp(x, y, z)*2
    #print(SA)

print(SA)

#TODO
# make function that detects adjacents - think it works
# for each adjacent subtract 2 sides, each cube starts with 6 - i dunno if this works properly?
# need some way to compare each cube against all other ones without taking too much time - prob good idk
# 3D list - acts as a 3D model? - YES
# compare model[x][y][z] with model[x+-1][y+-1][z+-1] - 6 comparisons which makes sense
# now to figure out how to make a 3D model in python - DONE

#past 1: 4446 *adjusted bounds in comp
#past 2: 4404 *see above but i actually used brain hopefully
#past 3: 4328 (too low or smth? idk why is this wrong - there are no duplicate coords in case that was possible)

#real: 4332 - somehow i'm down by 4 sides exactly? dunno how this happened