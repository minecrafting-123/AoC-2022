with open('input.txt', 'r') as reader:
    input = {tuple(int(num) for num in (line.strip().split(","))) for line in reader.readlines()}

ans = 0
for (x, y, z) in input:
    directions = {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}
    ans += len(directions.difference(input))

print(ans)