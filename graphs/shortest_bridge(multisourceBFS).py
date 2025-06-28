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
                # to break out of inner loop
                if grid[i][j] == 1:
                    break
            # to break out of outer loop
            if grid[i][j] == 1:
                break

        # this will make 1st island '2' and the other island remains as is
        dfs(i, j, bfs_q)
        print(f"Grid: {grid}, bfd_q: {bfs_q}")
        distance = 0

        # In this BFS we take the whole island as a node.. pretty cool. Read the problem in leetcode and try to visualise
        while bfs_q:
            new_bfs = deque([])
            # this loop iterates on the boundary of every newly created island in new_bfs
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