from collections import defaultdict
def longest_substring(s):
    d = defaultdict(int)
    l,r = 0, 0
    n = len(s)
    max_len = 0
    while r < n:
        d[s[r]] += 1
        if d[s[r]] == 1:
            max_len = max(max_len, r - l + 1)
        else:
            l = r
            d = defaultdict(int)
            d[s[r]] = 1
        r += 1
    return max_len

if __name__ == '__main__':
    s = input("Enter string: ")
    print(longest_substring(s))