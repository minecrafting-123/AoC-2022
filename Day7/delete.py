import re
cd = re.compile("cd (.+)")
d = re.compile("dir (.+)")
f = re.compile("[0-9]+ .+")

allTotals = []

class Object:
    def __init__(self, upper):
        self.upper = upper
    
class Directory(Object):
    def __init__(self, upper):
        super().__init__(upper)
        self.dictionary = {}
        self.dirTotal = 0
    def append(self, name, value):
        self.dictionary.update({name: value})
    def get(self, name):
        return self.dictionary.get(name)
    def add(self, value):
        self.dirTotal += int(value)
    def __str__(self):
        return self.dictionary.keys()[0]

class File(Object):
    def __init__(self, upper, value):
        super().__init__(upper)
        self.value = value
    def __str__(self):
        return self.value

main = Directory(None)
main.append("/", Directory(main))
currentDirectory = main

with open("input.txt") as reader:
    for line in reader:
        if(d.search(line) != None):
            dirValue = d.findall(line)[0]
            currentDirectory.append(dirValue, Directory(currentDirectory))
        elif (cd.search(line) != None):
            cdValue = cd.findall(line)[0]
            if (cdValue == ".."):
                currentDirectory.upper.add(currentDirectory.dirTotal)
                allTotals.append(currentDirectory.dirTotal)
                currentDirectory = currentDirectory.upper
            else:
                currentDirectory = currentDirectory.get(cdValue)
        elif (f.search(line) != None):
            fValue, fName = f.findall(line)[0].split(" ")
            currentDirectory.append(fName, File(currentDirectory, fValue))
            currentDirectory.add(fValue)

while(currentDirectory != main):
    currentDirectory.upper.add(currentDirectory.dirTotal)
    allTotals.append(currentDirectory.dirTotal)
    currentDirectory = currentDirectory.upper

smol = 70000000
needs = main.get("/").dirTotal - 40000000
for value in allTotals:
    if (value <= smol and value >= needs):
        smol = value

print(smol)