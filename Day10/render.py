import re
cycle = 0
register = 1

noop = re.compile("noop")
addx = re.compile("^addx (-?\d+)$")

def draw():
    if (cycle % 40 == 0):
        print("new")
    if (cycle % 40 == register or cycle % 40 == register + 1 or cycle % 40 == register - 1):
        print("#", end="")
    else:
        print(".", end="")

with open("input.txt") as reader:
    for line in reader:
        if (noop.search(line) != None):
            draw()
            cycle += 1
        elif (addx.search(line) != None):
            val = addx.findall(line)[0]
            draw()
            cycle += 1
            draw()
            cycle += 1
            register += int(val)