# find the number of subarrays with sum k, subarrays can have both positive, negative numbers and k can be both positive and negative
from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    total, cnt = 0, 0
    d = defaultdict(int)
    d[0] = 1
    for n in nums:
        total += n
        cnt += d[total-k]
        d[total] += 1
    return cnt

# sub-optimal solution
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         for i in range(1,n):
#             nums[i] = nums[i-1] + nums[i]
#         j, cnt = 0, 0
#         d = defaultdict(int)
#         d[0] = 1
#         while j < n:
#             cnt += d[nums[j] - k]
#             d[nums[j]] += 1
#             j += 1
#         return cnt