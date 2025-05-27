# longest subarray with sum <= k solved using Sliding window
# O(n)
def longest_subarray(arr, k):
    l, r= 0, 0
    sum = 0
    n = len(arr)
    max_len = 0
    lb, ub = n+1, 0
    while r < n and l < n:
        sum += arr[r]
        if sum <= k:
            max_len = max(max_len, r-l+1)
            if r - l + 1 > ub - lb + 1:
                lb, ub = l, r
        while sum > k:
            sum -= arr[l]
            l += 1
        r += 1
    return max_len, (lb, ub)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter the desired sum: "))
    print(longest_subarray(arr, k))


