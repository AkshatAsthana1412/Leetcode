from collections import defaultdict
edges = [(0,1),(0,3),(1,2),(3,4),(3,6),(3,7),(4,5),(4,2), (5,2)]
graph = defaultdict(list)
for (k,v) in edges:
    graph[k].append(v)

print(graph)

def path_exists(start, end, visited=[]):
    if start == end:
        return True
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            if path_exists(node, end, visited): # if instead I did "return path_exists(...)"" it would only check for 1 possible path and return it's result
                return True                     # as soon as it reaches a terminal node, which will not give the correct result.
    return False

print(path_exists(3,1))