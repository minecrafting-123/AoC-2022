import re, math
order = re.compile("[A-Z] [0-9]+")

visited = set()

class Rope:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self, xChange, yChange):
        self.x = self.x + xChange
        self.y = self.y + yChange

head = Rope(0, 0)
tail = Rope(0, 0)

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
            xMove = head.getX() - tail.getX()
            yMove = head.getY() - tail.getY()

            if (xMove ** 2 + yMove ** 2 > 4):
                if (xMove > 0 and yMove > 0):
                    tail.move(1, 1)
                elif (xMove > 0 and yMove < 0):
                    tail.move(1, -1)
                elif (xMove < 0 and yMove > 0):
                    tail.move(-1, 1)
                elif (xMove < 0 and yMove < 0):
                    tail.move(-1,-1)
            elif(xMove ** 2 + yMove ** 2 > 2):
                if (xMove > 0):
                    tail.move(1, 0)
                elif (xMove < 0):
                    tail.move(-1, 0)
                elif (yMove > 0):
                    tail.move(0, 1)
                elif (yMove < 0):
                    tail.move(0, -1)
            visited.add((tail.getX(), tail.getY()))

print(len(visited))