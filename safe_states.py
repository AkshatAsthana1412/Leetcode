from collections import deque, defaultdict
from build_graph import DirectedGraph
from kahn_algorithm import topological


if __name__ == '__main__':
    G = DirectedGraph().build_graph().reverse_graph()
    topo = topological(G.get_graph(), G.get_number_nodes())
    print(sorted(topo))
