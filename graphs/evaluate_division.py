from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        n = len(equations)
        for i in range(n):
            u, v = equations[i]
            weight = values[i]
            g[u].append((v, weight))
            g[v].append((u, 1.0/weight))
        
        def get_weight(start, end, visited):
            if start == end:
                return 1.0
            visited.append(start)
            res = 0
            for neighbor, weight in g[start]:
                if neighbor not in visited:
                    res = weight * get_weight(neighbor, end, visited)
                    if res != 0:
                        return res
            return 0


        ans = []
        for start, end in queries:
            if start not in g:
                ans.append(-1)
            else:
                visited = []
                w = get_weight(start, end, visited)
                ans.append(w if w!=0 else -1)
        return ans