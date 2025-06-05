from collections import defaultdict
# Sliding window, because we have to maintain the state of the window at each step
# and find the longest substring satisfying the condition
# O(n)
def lengthOfLongestSubstring(s: str) -> int:
    d = defaultdict(int)
    l, r = 0, 0
    max_len = 0
    n = len(s)
    while r < n:
        d[s[r]] += 1
        if d[s[r]] > 1:
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
        else:
            max_len = max(max_len, r-l+1)
        r += 1
    return max_len

print(lengthOfLongestSubstring('abcabccbb'))