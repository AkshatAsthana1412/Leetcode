from typing import List
from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i in range(n):
            if i != headID:
                g[manager[i]].append((i, informTime[i]))
        q = deque([(headID, 0)])
        max_time = 0
        while q:
            u, time = q.pop()
            max_time = max(max_time, time)
            for emp, t in g[u]:
                q.appendleft((emp, t+time))
        return max_time
    
# DFS solution
# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         g = defaultdict(list)
#         for i in range(n):
#             if manager[i] != -1:
#                 g[manager[i]].append(i)
#         max_time = 0 
#         def dfs(node, time=0):
#             nonlocal max_time
#             time += informTime[node]
#             max_time = max(max_time, time)
#             for emp in g[node]:
#                 dfs(emp, time)

#         dfs(headID)
#         return max_time


# Refactored DFS approach
# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         g = defaultdict(list)
#         for i in range(n):
#             if manager[i] != -1:
#                 g[manager[i]].append(i)
        
#         def dfs(node, time):
#             time += informTime[node]
#             if not g[node]:
#                 return time
#             max_time = 0
#             for emp in g[node]:
#                 max_time = max(max_time, dfs(emp, time))
#             return max_time
#         return dfs(headID, 0)