# initial solution
import math
from collections import deque
class Solution:
    def shortestBridge(self, grid: list) -> int:
        n = len(grid)
        def dfs(i, j, q):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i,j))
            for a, b in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                dfs(a, b, q)

        bfs_q = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    break
            if grid[i][j] == 1:
                break

        dfs(i, j, bfs_q)

        # print(f"Grid: {grid}, bfd_q: {bfs_q}")
        distance = 0
        while bfs_q:
            new_bfs = deque([])
            for i,j in bfs_q:
                for p,q in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if p >= 0 and p < n and q >= 0 and q < n:
                        if grid[p][q] == 1:
                            return distance
                        elif grid[p][q] == 0:
                            grid[p][q] = -1
                            new_bfs.append((p,q))
            bfs_q = new_bfs
            distance += 1
        return distance

    
l = [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
print(Solution().shortestBridge(l))