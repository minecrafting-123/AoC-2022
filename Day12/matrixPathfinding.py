import numpy as np
from scipy import sparse

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

start_coord = np.where(maze.flatten() == 'S')[0][0]
end_coord = np.where(maze.flatten() == 'E')[0][0]

maze[np.where(maze == 'S')] = 'a'
maze[np.where(maze == 'E')] = 'z'

nr_of_fields = maze.shape[0] * maze.shape[1]
    # build an adjacency? matrix to document which fields can be reached from which in one step
adj_matrix = np.zeros((nr_of_fields, nr_of_fields))

def find_reachable_neighbors(grid, i, j):
    neighbors = []
    grid_length, grid_width = grid.shape
    current_value = grid[i][j]
    if 0 < i and \
        ord(grid[i-1][j]) <= ord(current_value) + 1:
        neighbors.append((i-1)*grid_width + j)
    if i + 1 < grid_length and \
        ord(grid[i+1][j]) <= ord(current_value) + 1:
        neighbors.append((i+1)*grid_width + j)
    if 0 < j and \
        ord(grid[i][j-1]) <= ord(current_value) + 1:
        neighbors.append(i*grid_width + j - 1)
    if j + 1 < grid_width and \
        ord(grid[i][j+1]) <= ord(current_value) + 1:
        neighbors.append(i*grid_width + j + 1)
    return neighbors

for i in np.arange(maze.shape[0]):
    for j in np.arange(maze.shape[1]):
        neighbors_indices = find_reachable_neighbors(maze, i, j)
        np.put(adj_matrix[i*maze.shape[1] + j], neighbors_indices, 1)

target_matrix = sparse.csr_matrix(adj_matrix)
adj_matrix = sparse.csr_matrix(adj_matrix)
steps = 1
while (target_matrix.toarray()[start_coord, end_coord] == 0).all() and steps < 500:
    if steps % 30 == 0:
        print(f"{steps=}")
    target_matrix = target_matrix @ adj_matrix
    steps += 1
print(steps)

