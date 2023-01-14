#RegEx for integers
import re
p = re.compile("move ([0-9]+) from ([0-9]) to ([0-9])")

stuff = []
stacks = [[], [], [], [], [], [], [], [], []]
BASE_HEIGHT = 8
#reads file into stuff[]
with open("input.txt") as reader:
    for line in reader.readlines():
        stuff.append(line)
#splits stuff into two arrays, one with the boxes and one with directions
for thing in stuff:
    if (thing == "\n"):
        index = stuff.index(thing)
        break
boxes = stuff[:index]
directions = stuff[index:]
#function to turn read input from file into usable information
def translate(input):
    splitList = input.split(" ")
    finalList = []
    counter = 0
    for a in splitList:
        a = a.strip('\n')
        if (a == ""):
            counter += 1
            if (counter == 4):
                finalList.append("")
                counter = 0
        else:
            finalList.append(a)
            counter = 1
    return finalList
#creates 2-d array with each column as an entry
for n in range(BASE_HEIGHT-1, -1, -1):
    for i in range(len(translate(boxes[n]))):
        stacks[i].append(translate(boxes[n])[i])
#removes all the filler spaces from earlier translate
for i in range(len(stacks)):
    count = 0
    for thing in stacks[i]:
        if (thing == ""):
            count += 1
    for n in range(count):
        stacks[i].remove("")
directions.pop(0)
#moves stuff
def execute(amount, start, end):
    temp = stacks[start][-amount::1]
# VERY IMPORTANT/FUNNY? IF YOU REMOVE THIS LOOP WITH POP, EVERYTHING(most thing) BECOMES Z
#WHYYYYYYY??????????
    for i in range(amount):
        stacks[start].pop()
    stacks[end] += temp
#reads directions and executes them with above function
for line in directions:
    numbers = p.findall(line)
    amount = int(numbers[0][0])
    start = int(numbers[0][1])-1
    end = int(numbers[0][2])-1
    execute(amount, start, end)
#prints top numbers
for line in stacks:
    print(line[-1])