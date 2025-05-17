from graph_node import GraphNode
from collections import defaultdict


edges = [(0,1),(0,3),(1,2),(3,4),(3,6),(3,7),(4,5),(4,2)]
graph = defaultdict(list)
for edge in edges:
    k, v = edge
    graph[k].append(v)

def dfs(start, graph, visited=[]):
    print(start)
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node, graph, visited)

dfs(0, graph)
