with open("input.txt", 'r') as reader:
    original = [int(line.strip()) for line in reader.readlines()]
#there are duplicates, which makes this more annoying...wait does it? is it possible for an order swap to even happen? i don't think so rn
#which means all i need to do is keep track of what values have moved and it should be possible? current idea: make another boolean list for that, and move values in both lists
#yeah, the order can't change, so keeping track of values moved is all that is required pogU
moved = 0

part1 = original.copy()
moveOrder = [i for i in range(len(part1))]

def move(valueList, moveList, index):
    toMove = valueList.pop(index)
    newIndex = (toMove + index) % (len(valueList))
    #to wrap around correctly
    if newIndex == 0 and index != newIndex:
        newIndex = len(valueList)
    valueList.insert(newIndex, toMove)
    moveList.insert(newIndex, moveList.pop(index))


for order in range(len(part1)):
    i = moveOrder.index(order)
    move(part1, moveOrder, i)

zeroIndex = part1.index(0)
ans = part1[(zeroIndex + 1000) % len(part1)] + part1[(zeroIndex + 2000) % len(part1)] + part1[(zeroIndex + 3000) % len(part1)]
print(ans)

#try1: 11198 too high
#try2: 3466 correct!

KEY = 811589153

part2 = original.copy()

for i, value in enumerate(part2):
    part2[i] = value * KEY

moveOrder2 = [i for i in range(len(part2))]

for mix in range(10):
    for order in range(len(part2)):
        i = moveOrder2.index(order)
        move(part2, moveOrder2, i)
    #print(part2)
zeroIndex = part2.index(0)
ans2 = part2[(zeroIndex + 1000) % len(part2)] + part2[(zeroIndex + 2000) % len(part2)] + part2[(zeroIndex + 3000) % len(part2)]

#print(part2[(zeroIndex + 1000) % len(part2)], part2[(zeroIndex + 2000) % len(part2)], part2[(zeroIndex + 3000) % len(part2)])
print(ans2)

#try1: -8494092075298 
#try2: 9995532008348

#I did it!!!!!!!!