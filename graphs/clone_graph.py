from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node.val == 0:
            return Node()
        cp = {node:Node(node.val)}
        q = deque([node])
        visited = [node]
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.append(neighbor)
                    cp[neighbor] = Node(neighbor.val)
                cp[n].neighbors.append(cp[neighbor])
                
        return cp[node]