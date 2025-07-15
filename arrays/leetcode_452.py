# Minimum number of arrows to burst balloons
# Intervals concept, keep maintaining an intersection of intervals, all balloons within this intersection can be 
# burst by a single arrow, as soon as a new interval comes which has no intersection with this running
# interval, increment count by 1
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        last_end = points[0][1]
        last_start = points[0][0]
        cnt = 1
        for p in points:
            if p[0] <= last_end:
                last_start = max(last_start, p[0])
                last_end = min(last_end, p[1])
            else:
                cnt += 1
                last_start, last_end = p[0], p[1]
        return cnt