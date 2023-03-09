import re
cycle = 0
register = 1
totalStrength = 0

noop = re.compile("noop");
addx = re.compile("^addx (-?\d+)$");

def cycleCheck():
    global totalStrength
    if (cycle <= 220 and cycle % 40 == 20):
        totalStrength += cycle * register;

with open("input.txt") as reader:
    for line in reader:
        if (noop.search(line) != None):
            cycle += 1
            cycleCheck()
        elif (addx.search(line) != None):
            val = addx.findall(line)[0];
            print(val)
            cycle += 1
            cycleCheck()
            cycle += 1
            cycleCheck()
            register += int(val)
            
print(totalStrength)