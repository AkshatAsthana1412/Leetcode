def dfs(node, g, visited=[]):
    visited.append(node)
    if node in g:
        for adj_node in g[node]:
            if adj_node not in visited:
                dfs(adj_node, g, visited)
    return visited

def no_of_components(g):
    visited = []
    comp = 0
    for key in g.keys():
        if key not in visited:
            comp += 1
            visited = dfs(key, g, visited)
    return comp

if __name__ == "__main__":
    m = int(input("Enter the no. of edges: "))
    g = {}
    for _ in range(m):
        k, v = list(map(int, input("Enter edge: ").split()))
        try:
            g[k].append(v)
        except KeyError:
            g[k] = [v]
    print(f"No. of connected components: {no_of_components(g)}")
