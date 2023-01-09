elves = []
totalCalories = 0
bigElf = 0
bigElf2 = 0
bigElf3 = 0

with open('input.txt') as reader:
    for line in reader.readlines():
        if line == "\n":
            elves.append(totalCalories)
            totalCalories = 0
        else:
            totalCalories += int(line)
        
for elf in elves:
    if elf >= bigElf:
        bigElf = elf
elves.remove(bigElf)
for elf in elves:
    if elf >= bigElf2:
        bigElf2 = elf
elves.remove(bigElf2)
for elf in elves:
    if elf >= bigElf3:
        bigElf3 = elf

print(bigElf + bigElf2 + bigElf3)
