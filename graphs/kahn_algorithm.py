from collections import deque, defaultdict
# kahn's algorithm is basically topological sort with bfs

def is_cycle(g, n):
    # if a topo sort generates n elements, it is a DAG else THERE IS A CYCLE
    # to find a cycle we also don't need the topo sort list, we can simply keep a count of 
    # number of elements visited by topo sort
    return len(topological(g, n)) < n

def topological(g:dict, n:int):
    indegree = [0]*n
    for k in g.keys():
        for node in g[k]:
            indegree[node] += 1

    q = deque([])

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo_sort = []
    while q:
        node = q.popleft()
        topo_sort.append(node)
        for adj_node in g[node]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                q.append(adj_node)

    return topo_sort

if __name__ == '__main__':
    n = 6
    # g = defaultdict(list, {5:[0, 2], 4:[0, 1], 3:[1], 2:[3]})
    g = defaultdict(list, {1:[2], 2:[0, 3], 4:[5], 5:[3], 3:[4]})
    print(is_cycle(g,n))
    print(topological(g, n))