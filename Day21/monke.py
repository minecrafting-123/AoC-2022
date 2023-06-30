import re
monkeybook = {}
with open("input.txt", "r") as reader:
    monkeys = [line.strip().split(": ") for line in reader.readlines()]
    for name, action in monkeys:
        monkeybook[name] = action

#first thought is a recursive function, don't think i need to define a call stack for this one? I might do so anyways because it seems faster than recursion
#doing recursion because easier to understand

def get(monkey):
    #if it's a number monkey
    print(monkey)
    if re.findall("^(\d+)", monkeybook[monkey]):
        return int(monkeybook[monkey])
    monkeyParts = re.findall("^([a-z]+) (.) ([a-z]+)", monkeybook[monkey])[0]
    print(monkeyParts)
    
    print(monkeybook[monkey])
    return eval()

print(get("fchg"), get("hjpd"))

#eval() is the literal execution