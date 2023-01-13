overlaps = 0

with open("input.txt") as reader:
    for line in reader.readlines():
        first, last = line.split(",")
        a, b = first.split("-")
        c, d = last.split("-")
        if (not(int(b) < int(c) or int(a) > int(d))):
            overlaps += 1

print(overlaps)
