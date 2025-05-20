import heapq
import math
from build_graph import UndirectedGraph, DirectedGraph

# NOTE Dijktstra is not applicable for negative weights
def dijkstra(start:int, graph:dict, n:int):
    dist = [math.inf]*n
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, node = heapq.heappop(q)
        for adj_node, w in graph[node]:
            if w + d < dist[adj_node]:
                heapq.heappush(q, (w+d, adj_node))
                dist[adj_node] = w+d
    return dist

if __name__ == '__main__':
    G = UndirectedGraph(weighted = True)
    g = G.build_graph(use_csv=True, file_path="dijkstra_test.csv").get_graph()
    n = G.get_number_nodes()
    sn = int(input("Enter the start node: "))
    print(dijkstra(sn, g, n))


