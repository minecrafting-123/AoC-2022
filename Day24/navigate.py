#here's the plan: try to move all 5 possibilities, and add 1 time(t) each move attempt 
#find min time dunno how viable this is because infinite loop hmmmmmm
field = [line.strip() for line in open('input.txt').readlines()]
grid = {(x, y): c for y, l in enumerate(field)
                  for x, c in enumerate(l)}
