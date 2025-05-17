from collections import defaultdict
g = {}
g[2] = [3]
g[3] = [1]
g[5] = [0, 2]
g[4] = [0, 1]
g[3] = [1]
visited = []
s = []
def dfs(start):
    visited.append(start)
    if start in g:
        for node in g[start]:
            if node not in visited:
                dfs(node)
    s.append(start)

def topological_sort(g):
    for start in g:
        if start not in visited:
            dfs(start)
    return s[::-1]

print(topological_sort(g))
