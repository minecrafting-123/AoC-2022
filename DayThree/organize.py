sacks = []
prioSum = 0

with open('input.txt') as reader:
    for line in reader.readlines():
        sacks.append(line)
for sack in sacks:
    i = len(sack)
    str1 = sack[0:i//2]
    str2 = sack[i//2:]
    a = list(set(str1)&set(str2))
    for i in a:
        if (65 <= ord(i) <= 90):
            prioSum += ord(i) - 38
        elif(61 <= ord(i) <= 122):
            prioSum += ord(i) - 96
print(prioSum)