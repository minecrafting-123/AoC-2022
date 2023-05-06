import re

ROUNDS = 10000

class Monkey:
    def __init__(self, stuff, op, div, tru, fals):
        self.stuff = stuff[0].split(", ")
        self.op = op
        self.div = div
        self.tru = tru
        self.fals = fals
        self.inspects = 0
    def getStuff(self):
        return self.stuff
    def addStuff(self, add):
        self.stuff.append(add)
    def monkeyAround(self, bigDiv):
        toBeRemoved = list(())
        for thing in self.stuff:
            self.inspects += 1
            old = int(thing)
            new = eval(str(self.op))
            new = new % bigDiv
            if (new % self.div == 0):
                monkeyList[self.tru].addStuff(new)
                toBeRemoved.append(thing)
            else:
                monkeyList[self.fals].addStuff(new)
                toBeRemoved.append(thing)
        for element in toBeRemoved:
            self.stuff.remove(element)
    def getInspects(self):
        return self.inspects
    def getDivs(self):
        return self.div

with open("input.txt", 'r') as reader:
    monkeyList = list(())
    for monkey in reader.read().split("\n\n"):
        monkeset = monkey.split("\n")
        start = re.findall("^. Starting items: (\d+(?:[ \t]*,[ \t]*\d+)*$)", monkeset[1])
        operation = re.findall("^. Operation: new = (.+)", monkeset[2])
        test = re.findall("^. Test: divisible by (\d+)", monkeset[3])
        true = re.findall("^.   If true: throw to monkey (\d+)", monkeset[4])
        false = re.findall("^.   If false: throw to monkey (\d+)", monkeset[5])
        monke = Monkey(start, operation[0], int(test[0]), int(true[0]), int(false[0]))
        monkeyList.append(monke)

    divSum = 1
    for monkey in monkeyList:
        divSum *= monkey.getDivs()
    for x in range(ROUNDS):
        for monkey in monkeyList:
            monkey.monkeyAround(divSum)
    
    for monkey in monkeyList:
        #print(monkey.getStuff())
        print(monkey.getInspects())