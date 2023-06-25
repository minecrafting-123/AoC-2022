import re, copy
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]
blueprints = []
#A blueprint in the format of [ore, clay, [obi], [geode]] obi and geode are lists because there are multiple reqs
for line in lines:
    importantPart = line.split(": ")[1].strip()
    numbers = re.findall('\d+', importantPart)
    blueprints.append([[int(numbers[0]), 0, 0, 0], [int(numbers[1]), 0, 0, 0], [int(numbers[2]), int(numbers[3]), 0, 0], [int(numbers[4]), 0, int(numbers[5]), 0]])

#reqs are in form [ore, ore, [ore, clay], [ore, obi]]
#Crafting a robot takes materials at the START of a block, and completes it at the END of a block

startingResources = [0, 0, 0, 0] #ore, clay, obi, geode
startingRobots = [1, 0, 0, 0] #ore, clay, obi, geode

def buildTime(resources, robots, blueprint, robot):
    #returns the time and resources when the robot BECOMES AVAILABLE (day after building)
    t = 1
    for i in range(3):
        #if no robot to produce mat req
        if blueprint[robot][i] > 0 and robots[i] == 0:
            return None
        #if building is possible:
        reqResources = blueprint[robot][i] - resources[i]
        #if time is required to get enought resources for building
        if reqResources > 0:
            #from btrotta/advent-of-code-2022/day19a.py, using negative numbers and floor division to simulate "ceiling division"
            reqTime = -(-reqResources // robots[i]) + 1
            t = max(t, reqTime)
    newResources = copy.deepcopy(resources)
    for i in range(4):
        newResources[i] += t * robots[i] - blueprint[robot][i]
    return t, newResources
        


def step(resources, robots, blueprint, time):
    #check if can build
    #minute 24 occurs when time is 1, so building a geode robot then doesn't do anything - other than that always try to build a geode robot
    #print(resources, robots, time)
    if time == 0:
        possAnswers.add(resources[3])
        return
    usefulRobots = [3] if time > 1 else []
    for i, m in enumerate(maxNeededPerStep):
        if (time-1 > 0 and robots[i] + (resources[i] // (time-1)) < m):
            usefulRobots.append(i)
    #storing if a robot is buildable or not, and if it is, try building it
    canBuild = False
    for index in usefulRobots:
        x = buildTime(resources, robots, blueprint, index)
        if x is not None and time-x[0] > 0:
            canBuild = True
            newRobots = copy.deepcopy(robots)
            newRobots[index] += 1
            step(x[1], newRobots, blueprint, time-x[0])
    #happens at the end, where building a robot is no longer useful and you need to end da loop
    if canBuild == False:
        newResources = copy.deepcopy(resources)
        for i in range(4):
            newResources[i] += robots[i] * time
        step(newResources, robots, blueprint, 0)

ans = 0
for i, blueprint in enumerate(blueprints):
    maxNeededPerStep = [max([blueprint[robot][resource] for robot in range(4)]) for resource in range(4)]
    #print(maxNeededPerStep)
    possAnswers = {0}
    step(startingResources, startingRobots, blueprint, 24)
    ans += (i+1) * max(possAnswers)
print(ans)

ans2 = 1
for i in range(3):
    blueprint = blueprints[i]
    maxNeededPerStep = [max([blueprint[robot][resource] for robot in range(4)]) for resource in range(4)]
    possAnswers = {0}
    step(startingResources, startingRobots, blueprint, 32)
    ans2 *= max(possAnswers)
print(ans2)