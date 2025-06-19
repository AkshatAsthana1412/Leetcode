# important template: [Shrinking window]
# int i = 0, j = 0, ans = 0;
# for (; j < N; ++j) {
#     // CODE: use A[j] to update state which might make the window invalid
#     for (; invalid(); ++i) { // when invalid, keep shrinking the left edge until it's valid again
#         // CODE: update state using A[i]
#     }
#     ans = max(ans, j - i + 1); // the window [i, j] is the maximum window we've found thus far
# }
# return ans;
# 
# Essentially, we want to keep the window valid at the end of each outer for loop.

def freq(nums:list, k:int) -> int:
    i, j = 0, 0
    max_len, s = 0, 0
    n = len(nums)
    # IMPORTANT: ordering is not important to ge the answer here, so sorting is good.
    nums.sort()
    while j < n:
        s += nums[j]
        # here sorting helps us, because we always have the max element in the window as nums[j]
        while (j-i+1)*nums[j] - s > k:
            s -= nums[i]
            i += 1
        ans = max(ans, j-i+1)
        j += 1
    return ans
