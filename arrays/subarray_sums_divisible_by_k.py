from typing import List
from collections import defaultdict

# Concept: 
# given condition: 
# prefix_sum[j] - prefix_sum[i] = p * k  (p is a positive integer)
# taking mod with k on both sides:
#   prefix_sum[i] % k = prefix_sum[i] % k
# therefore it makes sense to keep a cache of prefix_sum[q] % k and 
# count will increase by the number of times the same remainder was seen before.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_cache = defaultdict(int)
        rem_cache[0] = 1
        rem = 0
        cnt = 0
        for n in nums:
            rem = ((rem+n)%k+k)%k
            cnt += rem_cache[rem]
            rem_cache[rem] += 1
        return cnt