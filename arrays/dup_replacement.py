from collections import defaultdict
def get_max_freq(d:dict):
    max_f = 0
    for key in d:
        max_f = max(max_f, d[key])
    return max_f

def duplicate_replacement(s:str, k:int):
    l, r = 0, 0
    max_len, max_f = 0, 0
    d = defaultdict(int)
    while r < len(s):
        d[s[r]] += 1
        max_f = max(max_f, get_max_freq(d))
        while (r-l+1) - max_f > k:
            d[s[l]] -= 1
            l += 1
        max_len = max(max_len, r-l+1)
        r += 1
    return max_len

print(duplicate_replacement('ABBCAACC', 2))