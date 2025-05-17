from collections import defaultdict

class Graph():
    def __init__(self, directed=False):
        self.g = defaultdict(list)
        self.n = 0
        self.directed = directed

    def __str__(self):
        return f"{self.g}"
    
    def get_graph(self):
        return self.g
    
    def build_graph(self):
        self.n = int(input("Enter the number of nodes: "))
        m = int(input("Enter the number of edges: "))
        for _ in range(m):
            k, v = list(map(int, input("Enter the edge: ").split()))
            self.g[k].append(v)
            if not self.directed:   
                self.g[v].append(k)
        return self
    
    def get_number_nodes(self):
        return self.n
    
class DirectedGraph(Graph):
    def __init__(self):
        super().__init__(directed=True)

    def reverse_graph(self):
        g_new = defaultdict(list)
        for node in self.g:
            for adj_node in self.g[node]:
                g_new[adj_node].append(node)
        self.g = g_new
        return self
        
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__(directed=False)
    