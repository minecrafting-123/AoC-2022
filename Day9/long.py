#copy follow code from rope.py
#assign each rope a "lead" in class
#head follows commands
#have a "visited" for only the last knot

import re, math
order = re.compile("[A-Z] [0-9]+")

ROPE_LENGTH = 10

visited = set()

class Rope:
    def __init__(self, x, y, lead):
        self.x = x
        self.y = y
        self.lead = lead
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self, xChange, yChange):
        self.x = self.x + xChange
        self.y = self.y + yChange
    def calcDif(self):
        self.xMove = self.lead.getX() - self.getX()
        self.yMove = self.lead.getY() - self.getY()
    def follow(self):
        if (self.xMove ** 2 + self.yMove ** 2 > 4):
            if (self.xMove > 0 and self.yMove > 0):
                self.move(1, 1)
            elif (self.xMove > 0 and self.yMove < 0):
                self.move(1, -1)
            elif (self.xMove < 0 and self.yMove > 0):
                self.move(-1, 1)
            elif (self.xMove < 0 and self.yMove < 0):
                self.move(-1,-1)
        elif(self.xMove ** 2 + self.yMove ** 2 > 2):
            if (self.xMove > 0):
                self.move(1, 0)
            elif (self.xMove < 0):
                self.move(-1, 0)
            elif (self.yMove > 0):
                self.move(0, 1)
            elif (self.yMove < 0):
                self.move(0, -1)

head = Rope(0, 0, None)

longRope = list()
longRope.append(head)

for i in range(ROPE_LENGTH-1):
    longRope.append(Rope(0, 0, longRope[i]))

with open("input.txt") as reader:
    for line in reader:
        inp = order.findall(line)[0].split(" ")
        direction, distance = inp[0], int(inp[1])
        for i in range(distance):
            if (direction == "L"):
                head.move(-1, 0)
            elif (direction == "R"):
                head.move(1, 0)
            elif (direction == "U"):
                head.move(0, 1)
            elif (direction == "D"):
                head.move(0, -1)
            for i in range(1, ROPE_LENGTH):
                longRope[i].calcDif()
                longRope[i].follow()
            #for i in range(ROPE_LENGTH):
            #    print(str(i) + "X: " + str(longRope[i].getX()) + " Y: " + str(longRope[i].getY()))

            visited.add((longRope[9].getX(), longRope[9].getY()))

print(len(visited))
