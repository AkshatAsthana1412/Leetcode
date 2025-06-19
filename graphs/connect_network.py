# return no. of edges that need to be realigned to make the graph connected
from collections import deque, defaultdict
from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        edges = len(connections)
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        
        state = [0]*n

        def bfs(start, cnt):
            state[start] = 1
            q = deque([start])
            while q:
                node = q.pop()
                for neighbor in g[node]:
                    if state[neighbor] == 1:
                        cnt += 1
                    elif state[neighbor] == 0:
                        state[neighbor] = 1
                        q.append(neighbor)
                state[node] = 2
            return cnt
        
        cnt = 0
        for i in range(n):
            if state[i] == 0:
                cnt = bfs(i, cnt)
        
        # Instead of this we can also return: num_components - 1
        return (n-1) - (edges-cnt)