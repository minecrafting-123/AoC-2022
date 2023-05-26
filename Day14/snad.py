import numpy as np
#Very cool way to read everything in a file and store it into an array
with open("input.txt", "r") as reader:
    lines = [entry.strip() for entry in reader.readlines()]

grid = np.zeros([1000, 200])
end_of_rock_field = 0
for line in lines:
    corners = line.split(' -> ')
    for i in range(len(corners) - 1):
        start_corner, end_corner = corners[i], corners[i+1]
        xs = [int(start_corner.split(',')[0]), int(end_corner.split(',')[0])]
        ys = [int(start_corner.split(',')[1]), int(end_corner.split(',')[1])]
        for x in range(min(xs), max(xs)+1):
            for y in range(min(ys), max(ys)+1):
                if y > end_of_rock_field:
                    end_of_rock_field = y
                grid[x, y] = 1

def add_snad():
    sand = (500, 0)
    while sand[1] <= end_of_rock_field:
        # down
        if grid[sand[0], sand[1]+1] == 0:
            sand = (sand[0], sand[1]+1)
        # left down
        elif grid[sand[0]-1, sand[1]+1] == 0:
            sand = (sand[0]-1, sand[1]+1)
        # right down
        elif grid[sand[0]+1, sand[1]+1] == 0:
            sand = (sand[0]+1, sand[1]+1)
        else:
            return sand
    return (-1, -1)
def add_snad_2():
    sand = (500, 0)
    bottom = end_of_rock_field + 2
    while sand[1] + 1 < bottom:
        if grid[sand[0], sand[1]+1] == 0:
            sand = (sand[0], sand[1]+1)
        # left down
        elif grid[sand[0]-1, sand[1]+1] == 0:
            sand = (sand[0]-1, sand[1]+1)
        # right down
        elif grid[sand[0]+1, sand[1]+1] == 0:
            sand = (sand[0]+1, sand[1]+1)
        else:
            return sand
    return sand
def part1():
    sand_tiles = 0
    new_sand = add_snad()
    while new_sand != (-1, -1):
        grid[new_sand[0], new_sand[1]] = 1
        sand_tiles += 1
        new_sand = add_snad()
    print(sand_tiles)

def part2():
    sand_tiles = 0
    new_sand = add_snad_2()
    while new_sand != (500, 0):
        grid[new_sand[0], new_sand[1]] = 1
        sand_tiles += 1
        new_sand = add_snad_2()
    print(sand_tiles + 1)

part2()