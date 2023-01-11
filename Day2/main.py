matchups = []
totalPoints = 0
with open('input.txt') as reader:
  for line in reader.readlines():
    string = line.strip()
    matchups.append(string)

for pair in matchups:
  a, b = pair.split(' ')
  if ((a == "A" and b == "Y") or (a == "B" and b == "X")
      or (a == "C" and b == "Z")):
    totalPoints += 1
  elif ((a == "A" and b == "Z") or (a == "B" and b == "Y")
        or (a == "C" and b == "X")):
    totalPoints += 2
  elif ((a == "A" and b == "X") or (a == "B" and b == "Z")
        or (a == "C" and b == "Y")):
    totalPoints += 3
  if (b == "X"):
    totalPoints += 0
  elif (b == "Y"):
    totalPoints += 3
  elif (b == "Z"):
    totalPoints += 6
print(totalPoints)
