from collections import deque
edges = [(0,1),(0,3),(1,2),(3,4),(3,6),(3,7),(4,5),(4,2), (5,2)]
graph = {}
for edge in edges:
    try:
        k, v = edge
        graph[k].append(v)
    except KeyError:
        graph[k] = [v]

def bfs(start, graph):
    q = deque([start])
    visited = [start]
    while q:
        node = q.popleft()
        print(node)
        if node in graph:
            for n in graph[node]:
                if n not in visited:
                    q.append(n)
                    visited.append(n)

bfs(0, graph)