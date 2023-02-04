import re
order = re.compile("[A-Z] [0-9]+")

visited = {}

class Rope:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self, x, y):
        self.x = x
        self.y = y

head = Rope(0, 0)
tail = Rope(0, 0)

with open("test.txt") as reader:
    for line in reader:
        inp = order.findall(line)[0].split(" ")
        direction, distance = inp[0], inp[1]
        for i in range(distance):
            if (direction == "L"):
                