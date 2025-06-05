from collections import defaultdict
# given conflicts b/w team member i, j. Check if the given team members can be distributed in 2 teams which have
# no conflicting developers in them
def dfs(g, node, color, colors):
    colors[node] = color
    for neighbor in g[node]:
        if colors[neighbor] == -1:
            dfs(g, neighbor, color, colors)

if __name__ == '__main__':
    n, m = int(input("Enter the no. of nodes ")), int(input("Enter the no. of conflicts "))
    conflicts = []
    for _ in range(m):
        u, v = list(map(int, input("Enter conflict as m n ").split()))
        conflicts.append([u,v])

    colors = [-1]*(n+1)
    g = defaultdict(list)

    for u, v in conflicts:
        g[u].append(v)
        g[v].append(u)

    color = 0
    for node in range(1, n+1):
        if colors[node] == -1:
            color += 1
            dfs(g, node, color, colors)
    
    if color > 1:
        print(True)
    else:
        print(False)
