from collections import defaultdict
# O(n)
def longest_substring(s):
    d = defaultdict(int)
    l,r = 0, 0
    n = len(s)
    max_len = 0
    while r < n:
        d[s[r]] += 1
        if d[s[r]] == 1:
            max_len = max(max_len, r - l + 1)
        while d[s[r]] > 1:
            d[s[l]] -= 1
            l += 1
        r += 1
    return max_len

if __name__ == '__main__':
    s = input("Enter string: ")
    print(longest_substring(s))