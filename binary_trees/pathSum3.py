# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, TreeNode
from collections import defaultdict
class Solution:           
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s, d):
            if not node:
                return 0
            if node:
                s += node.val
                # count for the current node
                cnt = d[s-targetSum]
                d[s] += 1
                # add count returned from the left subtree
                cnt += dfs(node.left, s, d)
                # add count returned from the right subtree
                cnt += dfs(node.right, s, d)
                # IMPORTANT: backtrack, decrement d[s] so that it doesn't pollute calculations for other 
                # branches. If we don't decrement d[s] in the current branch, then it might be incorrectly
                # considered while traversing another branch, which will return incorrect results
                d[s] -= 1
                return cnt
        d = defaultdict(int)
        d[0] = 1
        return dfs(root, 0, d)
# class Solution:
                
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         cnt = 0
#         def dfs(node, s, d):
#             nonlocal cnt
#             if node:
#                 s += node.val
#                 cnt += d[s-targetSum]
#                 d[s] += 1
#                 dfs(node.left, s, d)
#                 dfs(node.right, s, d)
#         d = defaultdict(int)
#         d[0] = 1
#         dfs(root, 0, d)
#         return cnt
        
