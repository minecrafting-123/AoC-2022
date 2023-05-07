maze = []

class Node():
    def __init__(self, position, distance=float("inf"), prev=None):
        self.position = position
        self.distance = distance
        self.prev = prev
    def __eq__(self, other):
        return self.position == other.position


#stores each letter into maze[][]
with open("input.txt", "r") as reader:
    for line in reader:
        maze.append(line.strip())
    for x, ele in enumerate(maze):
        newRow = []
        for letter in ele:
            newRow.append(letter)
        maze[x] = newRow



for row, val in enumerate(maze):
    for col, val2 in enumerate(maze[0]):
        if maze[row][col] == "S":
            start = Node((row, col), 0)
            maze[row][col] = "a"
        elif maze[row][col] == "E":
            end = Node((row, col))
            maze[row][col] = "z"



def isValid(OGrow, OGcol, row, col):
    return row >= 0 and col >= 0 and row < len(maze) and col < len(maze[0]) and (ord(maze[row][col]) <= ord(maze[OGrow][OGcol]) + 1)

def neighbors(row, col, dist):
    neighbors = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
    realNeighbors = []
    for (newRow, newCol) in neighbors:
        if isValid(row, col, newRow, newCol):
            realNeighbors.append(Node((newRow, newCol), dist+1))

    return realNeighbors
    

def bfs(start, end):
    queue = [start]
    visited = set()
    while len(queue) > 0:

        noders = queue.pop(0)
        if (noders.position in visited):
            continue

        visited.add(noders.position)

        for node in neighbors(noders.position[0], noders.position[1], noders.distance):
            if node == end:
                return node.distance
            if node.position not in visited:
                queue.append(node)

print(bfs(start, end))

#PART 2
starts = []
for row, val in enumerate(maze):
    for col, val2 in enumerate(maze[0]):
        if maze[row][col] == "a":
            start = Node((row, col), 0)
            starts.append(start)
lorge = float("inf")
for start in starts:
    if (bfs(start, end) == None):
        continue
    if (bfs(start, end) < lorge):
        lorge = bfs(start, end)
print(lorge)