import math
# O(n*m)
# def min_sum(i, j, grid, dp):
#     if i == 0 and j == 0:
#         return grid[i][j]
#     if i < 0 or j < 0:
#         return math.inf
#     if dp[i][j] != -1:
#         return dp[i][j]
#     up = grid[i][j] + min_sum(i-1, j, grid, dp)
#     left = grid[i][j] + min_sum(i, j-1, grid, dp)
#     dp[i][j] = min(left, up)
#     return dp[i][j]

def min_sum(m, n, grid):
    dp = [[-1]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                else:
                    up = math.inf
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                else:
                    left = math.inf
                dp[i][j] = min(up, left)
    return dp[m-1][n-1]

if __name__ == '__main__':
    m = int(input("Enter number of rows in grid "))
    n = int(input("Enter number of columns in grid "))
    grid = []
    for i in range(m):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        grid.append(row)
    dp = [[-1]*n for _ in range(m)]
    print(min_sum(m, n, grid))

