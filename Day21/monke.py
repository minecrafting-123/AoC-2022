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
    #print(monkey)
    if re.findall("^(\d+)", monkeybook[monkey]):
        return int(monkeybook[monkey])
    #if it's an operation monkey...
    #find the component monkeys
    monkeyParts = re.findall("^([a-z]+) . ([a-z]+)", monkeybook[monkey])[0]
    #print(monkeyParts)
    #calculate the values of the component monkeys
    locals()[monkeyParts[0]] = get(monkeyParts[0])
    locals()[monkeyParts[1]] = get(monkeyParts[1])
    #print(monkeybook[monkey])
    return eval(monkeybook[monkey])

print(get("root"))

#eval() is the literal execution
#try1: 70674280581468 FIRST TRY BABYYYYYYYY
# RECURSION FINALLY WORKED INSTEAD OF OVERLOADING WE WIN THESEEEEEEE
def get2(monkey):
    #if it's a number monkey
    #print(monkey)
    if re.findall("^(\d+)", monkeybook[monkey]):
        return int(monkeybook[monkey])
    #if it's an operation monkey...
    #find the component monkeys
    monkeyParts = re.findall("^([a-z]+) . ([a-z]+)", monkeybook[monkey])[0]
    #print(monkeyParts)

    #calculate the values of the component monkeys
    locals()[monkeyParts[0]] = get(monkeyParts[0])
    locals()[monkeyParts[1]] = get(monkeyParts[1])
    #print(monkeybook[monkey])
    return eval(monkeybook[monkey])
#part 2
#need to find the root half that doesn't include "humn" so i can try to set equal
rootParts = re.findall("^([a-z]+) . ([a-z]+)", monkeybook["root"])[0]

#how to do reverse calculations? some kind of indicator if a "route" includes "humn" maybe?
#man, if i could set a mathematical variable wouldn't that be nice... maybe i can somehow