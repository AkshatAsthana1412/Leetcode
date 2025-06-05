from typing import List
# Two pointers problem
# Here we're trying to get the max water in the container in a greedy way.
# We'll start with the window being the entire array, and keep shrinking the window to get better area value
# Since area = min(heights[l], heights[u]) * (u-l), and we know u-l is decreasing, so there's no point in optimising it
# we can only control min(heights[l], heights[u]) so we try get a higher value of this term, this motivates the movement 
# of l or u pointer.
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, u = 0, len(heights) - 1
        max_area = 0
        while l < u:
            area = min(heights[l], heights[u]) * (u-l)
            max_area = max(max_area, area)
            # try to get a higher value for heights[l] since height[u] is already good.
            if heights[l] < heights[u]:
                l += 1
            # else try to get a higher value for heights[u]
            else:
                u -= 1
        return max_area