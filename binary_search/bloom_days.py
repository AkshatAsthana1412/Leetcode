import math
def num_bouquets(day, bloom_days, k):
    cnt = 0
    m = len(bloom_days)
    b = 0
    i = 0
    while i < m:
        if bloom_days[i] <= day:
            cnt = cnt%k + 1
            i += 1
        else:
            cnt = 0
            while i < m and bloom_days[i] > day:
                i += 1
        b += cnt//k
    return b
    
def bloom_days(arr, n, k):
    if len(arr)//k < n:
        return -1
    min_day, max_day = min(arr), max(arr)
    l, u = min_day, max_day
    ans = math.inf
    while l <= u:
        day = (l+u)//2
        if num_bouquets(day, arr, k) >= n:
            ans = min(ans, day)
            u = day-1
        else:
            l = day+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    n = int(input("Enter the number of bouquets needed: "))
    k = int(input("Enter no. of flowers per bouquet: "))
    day = bloom_days(arr, n, k)
    print(f"Min no. of days needed: {day}")
