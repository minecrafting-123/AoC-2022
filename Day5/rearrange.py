stuff = []
stacks = []

with open("input.txt") as reader:
    for line in reader.readlines():
        stuff.append(line)

for thing in stuff:
    if (thing == "\n"):
        index = stuff.index(thing)
        break
boxes = stuff[:index]
directions = stuff[index:]

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
        
    print(splitList)
    print(finalList)

translate(boxes[2])
