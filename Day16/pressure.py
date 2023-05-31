import re
import functools
import collections as c
import itertools

#Extracts all the relavent values
with open("input.txt", "r") as reader:
    lines = [line.strip() for line in reader.readlines()]
valves = list(map(lambda line : re.findall("[^A-Z]*([A-Z]+)[^A-Z,^0-9]*(\d+)[^A-Z]+(.*)", line), lines))
#Initialize distance array for Floyd-Warshall
dist = c.defaultdict(lambda: 1000)
#All the valves with positive flow
names, flows = set(), dict()
#Preps distance array for Floyd-Warshall
for valve in valves:
    name, flow, connections = valve[0]
    names.add(name)
    if (int(flow) > 0):
        flows[name] = int(flow)
    for connect in connections.split(', '): dist[connect, name] = 1
#Floyd-Warshall 
for k, i, j in itertools.product(names, names, names):    # floyd-warshall
    dist[i,j] = min(dist[i,j], dist[i,k] + dist[k,j])
@functools.cache
def search(time, pos='AA', unvisitedValues=frozenset(flows), e=False):
    return max([flows[name] * (time - dist[pos, name] - 1) + search(time - dist[pos, name] - 1, name, unvisitedValues - {name}, e) for name in unvisitedValues if dist[pos, name] < time] + [search(26, unvisitedValues=unvisitedValues) if e else 0])
print(search(30), search(26, e=True))
