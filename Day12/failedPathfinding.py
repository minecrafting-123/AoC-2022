import numpy as np
#might use this for smth idk
class Node():
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

maze = []

#stores each letter into maze[][]
with open("input.txt", "r") as reader:
    for line in reader:
        maze.append(line.strip())
    for x, ele in enumerate(maze):
        newRow = []
        for letter in ele:
            newRow.append(letter)
        maze[x] = newRow
maze = np.array(maze)

startTuple = (int(np.where(maze == "S")[0]), int(np.where(maze == "S")[1]))
endTuple = (int(np.where(maze == "E")[0]), int(np.where(maze == "E")[1]))

startNode = Node(None, startTuple)
startNode.g = startNode.f = startNode.h = 0

endNode = Node(None, endTuple)
endNode.g = endNode.f = endNode.h = 0

maze[int(np.where(maze == "S")[0])][int(np.where(maze == "S")[1])] = "a"
maze[int(np.where(maze == "E")[0])][int(np.where(maze == "E")[1])] = "z"

openList = []
closedList = []

openList.append(startNode)

def return_path(currentNode):
    path = []
    count = 0
    current = currentNode
    while current is not None:
        path.append(current.position)
        count += 1
        current = current.parent
    return count

while(len(openList) > 0):

    currentNode = openList[0]
    print(currentNode.position)
    currentIndex = 0
    for index, item in enumerate(openList):
        if item.f < currentNode.f:
            currentNode = item
            currentIndex = index

    openList.pop(currentIndex)
    closedList.append(currentNode)

    if currentNode == endNode:
        return_path(currentNode)
    
    children = []
    for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nodePosition = (int(currentNode.position[0]) + newPosition[0], int(currentNode.position[1]) + newPosition[1])
        #might need to adjust this for (y, x) or (x, y)
        if nodePosition[0] > (int(len(maze)) - 1) or nodePosition[0] < 0 or nodePosition[1] > int(len(maze[int(len(maze))-1])-1) or nodePosition[1] < 0:
            continue
        if ord(str(maze[nodePosition[0]][nodePosition[1]])[0]) > ord(str(maze[currentNode.position[0]][currentNode.position[1]])[0]) + 1:
            continue
        newNode = Node(currentNode, nodePosition)
        children.append(newNode)
    
    for child in children:
        print(child.position)
        for closedChild in closedList:
            if child == closedChild:
                continue
        
        child.g = currentNode.g + 1
        child.h = ((child.position[0] - int(endNode.position[0]))) ** 2 + ((child.position[1] - int(endNode.position[1])) ** 2)
        child.f = child.g + child.h

        for openNode in openList:
            if child == openNode and child.g > openNode.g:
                continue
        
        openList.append(child)