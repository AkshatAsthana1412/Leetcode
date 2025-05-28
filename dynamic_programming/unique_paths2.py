# def unique_paths2(i, j, maze):
#     if i == 0 and j == 0:
#         return 1
#     if i < 0 or j < 0:
#         return 0
#     if maze[i][j] == -1:
#         return 0
#     up = unique_paths2(i-1, j, maze)
#     left = unique_paths2(i, j-1, maze)
#     return up + left

# tabulation
def unique_paths2(m, n, maze):
    dp = [ [-1]*n for _ in range(m) ]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif maze[i][j] == -1:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
            
if __name__ == "__main__":
    m = int(input("Enter number of rows in grid "))
    n = int(input("Enter number of columns in grid "))
    grid = []
    for i in range(m):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        grid.append(row)
    print(unique_paths2(m, n, grid))
