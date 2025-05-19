from build_graph import UndirectedGraph
from collections import deque


def bfs(start:int, n:int, g:dict) -> list:
    dist = [-1] * n
    q = deque([start])
    visited = [0] * n
    visited[start] = 1
    while q:
        node = q.popleft()
        for adj_node in g[node]:
            if not visited[adj_node]:
                dist[adj_node] = dist[node] + 1
                q.append(adj_node)
                visited[adj_node] = 1
    return dist

if __name__ == '__main__':
    G = UndirectedGraph().build_graph()
    n = G.get_number_nodes()
    g = G.get_graph()
    start = int(input("enter starting node: "))
    distances = bfs(start, n, g)
    print(distances)