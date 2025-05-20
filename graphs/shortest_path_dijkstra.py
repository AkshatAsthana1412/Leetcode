from collections import deque
from dijkstra_algorithm import dijkstra
from build_graph import UndirectedGraph

def shortest_path(start:int, end:int, graph:dict, n:int):
    _, prev_node = dijkstra(start, graph, n)
    q = deque([end])
    last_node = prev_node[end]
    while last_node != -1:
        q.appendleft(last_node)
        last_node = prev_node[last_node]
    return q

if __name__ == "__main__":
    G = UndirectedGraph(weighted = True)
    g = G.build_graph(use_csv=True, file_path="dijkstra_test.csv").get_graph()
    n = G.get_number_nodes()
    sn = int(input("Enter the start node: "))
    en = int(input("Enter the end node: "))
    print(shortest_path(sn, en, g, n))