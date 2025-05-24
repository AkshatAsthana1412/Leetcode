from typing import List
from collections import defaultdict
class Solution:

    # O(m * nlogn)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     d = dict()
    #     for s in strs:
    #         sorted_s = ''.join(sorted(s))
    #         try:
    #             d[sorted_s].append(s)
    #         except KeyError:
    #             d[sorted_s] = [s]
    #     return list(d.values())
    
    # O(m * n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            d[count].append(s)
        print(list(d.values()))
