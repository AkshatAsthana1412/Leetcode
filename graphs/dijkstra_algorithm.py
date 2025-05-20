import heapq
import math
from build_graph import UndirectedGraph, DirectedGraph
from collections import deque

# NOTE Dijktstra is not applicable for negative weights it leads to infinite loop becoz we'll keep on getting higher
# negative values continuously.
# NOTE time complexity: O(E*logV)
def dijkstra(start: int, graph: dict, n: int) -> list:
    """
    Compute the shortest path distances from the start node to all other nodes
    in a weighted graph using Dijkstra's algorithm.

    :param start: The source node
    :param graph: The adjacency list of the graph with weights
    :param n: The total number of nodes
    :return: List of shortest distances from start to each node
    """
    dist = [math.inf] * n
    dist[start] = 0
    min_heap = [(0, start)]
    prev_node = [-1]*n
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        # Not strictly necessary to use a `visited` set here:
        # With a priority queue-based Dijkstra, we may push a node multiple times,
        # but only the one with the minimal distance will update the dist array.
        # Adding a visited set could optimize performance by skipping finalized nodes.
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev_node[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return dist, prev_node



if __name__ == '__main__':
    G = UndirectedGraph(weighted = True)
    g = G.build_graph(use_csv=True, file_path="dijkstra_test.csv").get_graph()
    n = G.get_number_nodes()
    sn = int(input("Enter the start node: "))
    print(dijkstra(sn, g, n))