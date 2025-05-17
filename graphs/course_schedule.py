from collections import defaultdict
n = int(input("number of courses: "))
m = int(input("enter number of prerequisites: "))
edges = []
for _ in range(m):
    edge = list(map(int, input("Enter prerequisite: ").split()))
    edges.append(edge)

g = {}
for k,v in edges:
    try:
        g[k].append(v)
    except KeyError:
        g[k] = [v]

UNVISITED, VISITING, VISITED = 0, 1, 2
state = [UNVISITED]*n

def is_cycle(start):
    state[start] = VISITING
    if start in g:
        for node in g[start]:
            if state[node] == VISITING or is_cycle(node):
                return True
    state[start] = VISITED
    return False

flag = True
keys = g.keys()
for start in keys:
    if state[start] != VISITED:
        if is_cycle(start):
            flag = False
            break
print(flag)



