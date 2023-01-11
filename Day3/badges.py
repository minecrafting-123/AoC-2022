sacks = []
prioSum = 0

with open('input.txt') as reader:
    group = ""
    linecount = 0
    for line in reader.readlines():
        group += line.strip()
        group += " "
        linecount += 1
        if (linecount >= 3):
            linecount = 0
            sacks.append(group)
            group = ""

for sack in sacks:
    a, b, c = sack.split(" ", 2)
    common = list(set(a)&set(b)&set(c))
    for i in common:
        if (65 <= ord(i) <= 90):
            prioSum += ord(i) - 38
        elif(61 <= ord(i) <= 122):
            prioSum += ord(i) - 96
print(prioSum)