pairs = 0

with open("input.txt") as reader:
    for line in reader.readlines():
        first, last = line.split(",")
        a, b = first.split("-")
        c, d = last.split("-")
        if ((int(a) <= int(c) and int(b) >= int(d)) or (int(c) <= int(a) and int(d) >= int(b))):
            pairs += 1

print(pairs)

