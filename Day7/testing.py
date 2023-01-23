class Object:
    def __init__(self, current):
        self.currentDir = current
    
class Directory(Object):
    def __init__(self, current):
        super().__init__(current)
        self.dictionary = {}
    def append(self, name, value):
        self.dictionary.update({name: value})
    def __str__(self):
        return "dir"

main = Directory(None)
currentDirectory = main

if (currentDirectory.__str__() == "dir"):
    print("success")
else:
    print(":(")