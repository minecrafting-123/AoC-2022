import re

class Monkey:
    def __init__(self, stuff, op, div, tru, fals):
        self.stuff = stuff
        self.op = op
        self.div = div
        self.tru = tru
        self.fals = fals

    #EVAL FUNCTION ALLOWS FOR IN LINE CODE
with open("input.txt", 'r') as reader:
    monkeyList = list(())
    for monkey in reader.read().split("\n\n"):
        monkeset = monkey.split("\n")
        start = re.findall("^. Starting items: (\d+(?:[ \t]*,[ \t]*\d+)*$)", monkeset[1])
        operation = re.findall("^. Operation: new = (.+)", monkeset[2])
        test = re.findall("^. Test: divisible by (\d+)", monkeset[3])
        true = re.findall("^.   If true: throw to monkey (\d+)", monkeset[4])
        false = re.findall("^.   If false: throw to monkey (\d+)", monkeset[5])
        monke = new Monkey(start, operation, test, true, false)
        monkeyList.append(Monkey)
        