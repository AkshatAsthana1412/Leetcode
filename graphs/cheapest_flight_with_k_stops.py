from collections import deque
import math
from build_graph import UndirectedGraph

def dijkstra(g, n, k, start, end):
    from collections import deque
    import math

    q = deque()
    q.append((0, start, 0))  # (stops, node, total_distance)
    dist = [math.inf] * n
    dist[start] = 0

    while q:
        stops, node, total = q.popleft()

        if stops > k:
            continue  # too many stops

        for neighbor, weight in g[node]:
            new_total = total + weight

            # We allow a better distance OR more stops to explore alternative paths
            if new_total < dist[neighbor] and stops <= k:
                dist[neighbor] = new_total
                q.append((stops + 1, neighbor, new_total))

    return dist[end] if dist[end] != math.inf else -1

if __name__ == "__main__":
    G = UndirectedGraph(weighted=True).build_graph(use_csv=True, file_path="k_stops_test.csv")
    g, n = G.get_graph(), G.get_number_nodes()
    start, end, k = int(input("Enter start node: ")), int(input("Enter end node: ")), int(input("Enter the desired number of stops: "))
    print(dijkstra(g, n, k, start, end))

                