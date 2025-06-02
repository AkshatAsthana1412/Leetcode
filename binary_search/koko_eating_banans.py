import math
def get_time_taken(stack, rate):
    s = 0
    for i in stack:
        s += math.ceil(i/rate)
    return s

def koko_eating_bananas(stack, time_limit):
    mx = max(stack)
    l, u = 1, mx
    ans = math.inf
    while l <= u:
        m = (l+u)//2
        t = get_time_taken(stack, m)
        if t <= time_limit:
            ans = min(ans, m)
            u = m-1
        else:
            l = m+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    time_limit = int(input("Enter the time limit in which to eat the bananas: "))
    num = koko_eating_bananas(arr, time_limit)
    print(f"Min rate of eating bananas: {num}")
