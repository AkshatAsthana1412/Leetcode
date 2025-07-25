# Check if there exists a subsequence in arr whose sum = k
# O(2^n) for recursive solution

# def f(ind, target, arr):
#     if target == 0:
#         return True
#     if ind == 0:
#         return arr[ind] == target
#     found = f(ind-1, target-arr[ind], arr) or f(ind-1, target, arr)
#     return found

# arr = [1,2,3,4]
# n = len(arr)
# print(f(n-1, 9, arr))

# memoised solution O(n * target)
def search(ind, target, arr, dp):
    if target == 0:
        return True
    if ind == 0:
        return arr[ind] == target
    if dp[ind][target] != -1:
        return dp[ind][target]
    dp[ind][target] = search(ind-1, target-arr[ind], arr, dp) or search(ind-1, target, arr, dp)
    return dp[ind][target]

# arr = [8, 3, 9, 0, 4, 5, 7, 12]
# n = len(arr)
# dp = [[-1]*(10**3+1) for _ in range(10^3+1)]
# print(search(n-1, 290, arr, dp))

# tabulated solution
def search(target, arr):
    n = len(arr)
    dp = [[False]*(n) for _ in range(target+1)]
    for i in range(n):
        dp[i][0] = True
    dp[0][arr[0]] = True
    for i in range(1, n):
        for j in range(target, 0, -1):
            dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]
    return dp[n-1][target]

arr = [8, 3, 9, 0, 4, 5, 7, 12]
print(search(24, arr))