#make a function that converts from SNAFU to standard, convert every number, sum them all, 
#what if i just sum them all in SNAFU
#i'm going to try and sum starting from the 1s place, then idk do math i guess

listed = [[x for x in num.strip()] for num in open("input.txt").readlines()]

longest = 0
for number in listed:
    if len(number) > longest:
        longest = len(number)
print(longest)
digited = [[] for _ in range(longest)]
finalNum = []
for index in range(1, longest+1):
    for number in listed:
        if index <= len(number):
            digited[index-1].append(number[-index])

def sumPlace(placeList, carry):
    total = carry
    for digit in placeList:
        match digit:
            case '=': total -= 2
            case '-': total -= 1
            case _: total += int(digit)
    toNext = 0
    while total >= 3:
        toNext += 1
        total -= 5
    while total <= -3:
        toNext -= 1
        total += 5
    finalNum.append(total)
    return toNext
toNext = 0
for place in digited:
    toNext = sumPlace(place, toNext)
if toNext: finalNum.append(toNext)

ans = ""
for digit in finalNum:
    match digit:
        case -2: ans = '=' + ans
        case -1: ans = '-' + ans
        case _: ans = str(digit) + ans
print(finalNum, ans)
