# recursion solution O(2^(m*n))
# def unique_paths(i, j):
#     if i == 0 and j == 0:
#         return 1
#     if i < 0 or j < 0:
#         return 0
#     up = unique_paths(i-1, j)
#     left = unique_paths(i, j-1)
#     return up + left

# memoization O(m*n)
# def unique_paths(i, j, dp):
#     if i == 0 and j == 0:
#         return 1
#     if i < 0 or j < 0:
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]
#     up = unique_paths(i-1, j, dp)
#     left = unique_paths(i, j-1, dp)
#     dp[i][j] = up + left
#     return dp[i][j]

# tabulation
def unique_paths(m, n): 
    dp = [ [-1]*(n) for _ in range(m) ]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # print(dp)
    return dp[m-1][n-1]


if __name__ == "__main__":
    m = int(input("Enter number of rows in grid "))
    n = int(input("Enter number of columns in grid "))
    dp = [ [-1] * n for _ in range(m) ]
    print(unique_paths(m, n))
    # print(dp)