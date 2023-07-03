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
        return float(monkeybook[monkey])
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

#part 2
operationList = []
rootnum = 0
def get2(monkey):
    #if it's a number monkey
    #print(monkey)
    if monkey == "humn":
        return "humn"
    if re.findall("^(\d+)", monkeybook[monkey]):
        return float(monkeybook[monkey])
    #if it's an operation monkey...
    #find the component monkeys and operation
    monkeyParts = re.findall("^([a-z]+) (.) ([a-z]+)", monkeybook[monkey])[0]
    #first monkey, operation, second monkey
    #print(monkeyParts)
    #calculate the values of the component monkeys
    locals()[monkeyParts[0]] = get2(monkeyParts[0])
    locals()[monkeyParts[2]] = get2(monkeyParts[2])
    #print(locals()[monkeyParts[0]], locals()[monkeyParts[2]])
    #if "humn" then record operation being applied
    if locals()[monkeyParts[0]] == "humn":
        operationList.append((get(monkeyParts[2]), monkeyParts[1]))
        return "humn"
    if locals()[monkeyParts[2]] == "humn":
        if (monkeyParts[1] == "-"):
            operationList.append((get(monkeyParts[0]), "-."))
            return "humn"
        if (monkeyParts[1] == "/"):
            operationList.append((get(monkeyParts[0]), "/."))
            return "humn"
        operationList.append((get(monkeyParts[0]), monkeyParts[1]))
        return "humn"
    #print(monkeybook[monkey]
    return eval(monkeybook[monkey])

def reverseOperation(partnum, operation):
    global rootnum
    #x + p = r
    if operation == "+":
        rootnum -= partnum
    if operation == "-":
        rootnum += partnum
    if operation == "-.":
        rootnum = partnum - rootnum
    if operation == "*":
        rootnum /= partnum
    if operation == "/":
        rootnum *= partnum
    if operation == "/.":
        rootnum = partnum / rootnum

rootParts = re.findall("^([a-z]+) . ([a-z]+)", monkeybook["root"])[0]
root1, root2 = get2(rootParts[0]), get2(rootParts[1])
print(root1, root2)
if (root1 != "humn"):
    rootnum = root1
else:
    rootnum = root2
print(rootnum)

while operationList:
    partnum, operation = operationList.pop()
    print(rootnum, operation, partnum)
    reverseOperation(partnum, operation)
print(rootnum)

#try 1: 51164504202966 (too high)
#try 2:-1089.1550203110228 (i mean this is a decimal so no)
#try 3: 3243420789721 (I FORGOT TO CHANGE A NUMBER WHEN COPY AND PASTING)