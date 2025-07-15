# to remove minimum number of overlapping intervals, we should keep intervals with the earliest end times
# as this gives maximum room for subsequent intervals to fit without overlapping.
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = []
        cnt = 0
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        for it in intervals:
            if not ans:
                ans.append(it)
            elif it[0] < ans[-1][1] or it[1] <= ans[-1][1]:
                cnt += 1
                if it[1] < ans[-1][1]:
                    ans.pop()
                    ans.append(it)
            else:
                ans.append(it)
        return cnt
