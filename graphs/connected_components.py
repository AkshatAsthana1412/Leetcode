from build_graph import UndirectedGraph
def dfs(start:int, graph:dict, visited:set=set()) -> list:
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
    return visited

def connected_components(g:dict, n:int):
    cnt = 0
    visited = set()
    # it's always good to iterate over all nodes n, because it's possible 
    # that some nodes aren't connected to anyone and they won't show up in 
    # 'g', so the code will ignore them. So avoid doing: `for node in g:`
    for node in range(n):
        if node not in visited:
            cnt += 1
            visited = dfs(node, g, visited)
    return cnt

if __name__ == '__main__':
    G = UndirectedGraph()
    g = G.build_graph().get_graph()
    n = G.get_number_nodes()
    print(f"Number of connected components: {connected_components(g, n)}")