#from btrotta/advent-of-code-2022, which is how I check my answers and also helps me learn new things

import re, copy
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]
blueprints = []
#A blueprint in the format of [ore, clay, [obi], [geode]] obi and geode are lists because there are multiple reqs
for line in lines:
    importantPart = line.split(": ")[1].strip()
    numbers = re.findall('\d+', importantPart)
    blueprints.append([[int(numbers[0]), 0, 0, 0], [int(numbers[1]), 0, 0, 0], [int(numbers[2]), int(numbers[3]), 0, 0], [int(numbers[4]), 0, int(numbers[5]), 0]])

def get_time_to_build(blueprint, resources, robots, robot_ind):
    # find shortest time to build given robot (without building any other additional robots)
    # return time and resources at time robot becomes available
    t = 1
    for i_res in range(3):
        if blueprint[robot_ind][i_res] > 0 and robots[i_res] == 0:
            return None
        req_remaining = (blueprint[robot_ind][i_res] - resources[i_res])
        if req_remaining > 0:
            # "ceiling division", from https://stackoverflow.com/a/17511341
            time_to_collect = max(0, -(req_remaining // -robots[i_res]))
            t = max(t, time_to_collect + 1)
    new_resources = copy.deepcopy(resources)
    for i_res in range(4):
        new_resources[i_res] += t * robots[i_res] - blueprint[robot_ind][i_res]
    return t, new_resources


max_t = 24
ans = 0
for blueprint_ind, blueprint in enumerate(blueprints):
    best = 0
    to_visit = [[0, [1, 0, 0, 0], [0, 0, 0, 0]]]  # time, robots, resources
    # Maximum quantity needed of ore, clay and obsidian at each step. Since we can only
    # produce 1 robot at each step, any amount produced of these resources greater than the
    # maximum needed to build a robot is wasted.
    max_needed_per_step = [max([blueprint[i_robot][i_resource] for i_robot in range(4)]) for i_resource in range(4)]
    while len(to_visit) > 0:
        t, robots, resources = to_visit.pop()
        if t == max_t:
            best = max(best, resources[-1])
        else:
            # check which resources we have enough of already
            useful_robots = [3] if t < max_t - 1 else []
            for i, m in enumerate(max_needed_per_step[:3]):
                num_steps = max(0, max_t - t - 2)  # excluding final 2 steps
                if num_steps > 0 and robots[i] + (resources[i] // num_steps) < m:
                    useful_robots.append(i)
            can_build = False
            for robot_ind in useful_robots:
                x = get_time_to_build(blueprint, resources, robots, robot_ind)
                if x is not None:
                    new_robots = copy.deepcopy(robots)
                    new_robots[robot_ind] += 1
                    if x[0] + t < max_t:
                        to_visit.append([x[0] + t, new_robots, x[1]])
                        can_build = True
            if not can_build:
                new_resources = copy.deepcopy(resources)
                num_steps = max_t - t
                for i_res in range(4):
                    new_resources[i_res] += robots[i_res] * num_steps
                to_visit.append([max_t, robots, new_resources])
    ans += (blueprint_ind + 1) * best

print(ans)