from build_graph import DirectedGraph
import heapq
import math

def dijkstra(g, n, src, ways, dist):
    min_heap = []
    ways[src], dist[src] = 1, 0
    heapq.heappush(min_heap, (0, src))
    while min_heap:
        cur_dist, node = heapq.heappop(min_heap)
        for neighbor, w in g[node]:
            distance = cur_dist + w
            heapq.heappush(min_heap, (distance, neighbor))
            if distance < dist[neighbor]:
                ways[neighbor] = ways[node]
                dist[neighbor] = distance
            elif distance == dist[neighbor]:
                ways[neighbor] += ways[node] % 10**9
    return ways, dist

if __name__ == "__main__":
    G = DirectedGraph(weighted=True).build_graph(use_csv=True, file_path="k_stops_test.csv")
    g = G.get_graph()
    n = G.get_number_nodes()
    src = int(input("enter the source node: "))
    dest = int(input("enter the destination node: "))
    dist = [math.inf]*n
    ways = [0]*n
    ways, dist = dijkstra(g, n, src, ways, dist)
    print(f"Ways 1 array: {ways}, distance 1 array: {dist}")
    # ways, dist = dijkstra(g, n, src, [0]*n, dist)
    # print(f"Ways 2 array: {ways}, distance 2 array: {dist}")
    print(f"Ways to reach destination: {ways[dest]}")