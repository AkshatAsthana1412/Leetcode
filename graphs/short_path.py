from build_graph import Graph

g = Graph().build_graph().get_graph()

def s_path(g, start, end, path = []):
    # we want path variable to not maintain states across call stacks, so each call stach has it's own path variable, 
    # the comparison is done using sp and shortest_path variables which maintain states across stacks
    path = path + [start] 
    shortest_path = None
    if start == end:
        return path
    for node in g[start]:
        if node not in path:
            sp = s_path(g, node, end, path)
            if shortest_path is None or len(sp) < len(shortest_path):
                shortest_path = sp
    return shortest_path

start, end = list(map(int, input("Enter start and end node").split()))

print('->'.join(list(map(str, s_path(g, start, end)))))

        