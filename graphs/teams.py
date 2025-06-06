from collections import defaultdict, deque
# given conflicts b/w team member i, j. Check if the given team members can be distributed in 2 teams which have
# no conflicting developers in them
# Solved using Bipartite graph concept, i.e. no two adjacent nodes should be of the same color
def bfs(node, g, n):
    q = deque([node])
    colors[node] = 0
    colors = [-1]*(n+1)
    while q:
        node = q.popleft()
        for neighbor in g[node]:
            if colors[neighbor] == -1:
                colors[neighbor] = (colors[node]+1)%2
                q.append(neighbor)
            elif colors[node] == colors[neighbor]:
                return False
    return True
            
            

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
    ans = True
    for node in range(1, n+1):
        if colors[node] == -1:
            ans = ans and bfs(g, node, color, colors)
    
    print(f"Teams can be made: {ans}")
