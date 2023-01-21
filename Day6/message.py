marker = []
count = 0
MARKER_LENGTH = 14

def check():
    for i in range(len(marker)):
        for g in range(len(marker)):
            if not (g == i):
                if (marker[i] == marker[g]):
                    return False
    return True

with open("input.txt") as reader:
    for line in reader:
        for char in line:
            count += 1
            if (len(marker) < MARKER_LENGTH):
                marker.append(char)
            else:
                for i in range(len(marker)-1):
                    marker[i] = marker[i+1]
                marker[-1] = char
                if (check()):
                    print(count)
                    break
