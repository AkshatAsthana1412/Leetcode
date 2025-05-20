from collections import defaultdict
import csv

class Graph():
    def __init__(self, directed=False, weighted=False):
        self.g = defaultdict(list)
        self.n = 0
        self.directed = directed
        self.weighted = weighted

    def __str__(self):
        return f"{self.g}"
    
    def get_graph(self):
        return self.g
    
    def build_graph(self, use_csv=False, file_path=None):
        if use_csv and file_path:
            return self.build_graph_from_csv(file_path)
        
        self.n = int(input("Enter the number of nodes: "))
        m = int(input("Enter the number of edges: "))
        for _ in range(m):
            if self.weighted:
                k, v, w = map(int, input("Enter the edge and weight (u v w): ").split())
                self.g[k].append((v, w))
                if not self.directed:
                    self.g[v].append((k, w))
            else:
                k, v = map(int, input("Enter the edge (u v): ").split())
                self.g[k].append(v)
                if not self.directed:
                    self.g[v].append(k)
        return self

    def build_graph_from_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.n = int(header[0])  # Assume first row is "num_nodes"
            for row in reader:
                if self.weighted:
                    k, v, w = map(int, row)
                    self.g[k].append((v, w))
                    if not self.directed:
                        self.g[v].append((k, w))
                else:
                    k, v = map(int, row)
                    self.g[k].append(v)
                    if not self.directed:
                        self.g[v].append(k)
        return self
    
    def get_number_nodes(self):
        return self.n
    
class DirectedGraph(Graph):
    def __init__(self, weighted=False):
        super().__init__(directed=True, weighted=weighted)

    def reverse_graph(self):
        g_new = defaultdict(list)
        for node in self.g:
            for adj in self.g[node]:
                if self.weighted:
                    v, w = adj
                    g_new[v].append((node, w))
                else:
                    g_new[adj].append(node)
        self.g = g_new
        return self
    
class UndirectedGraph(Graph):
    def __init__(self, weighted=False):
        super().__init__(directed=False, weighted=weighted)