# m = int(input("Enter number of rows"))
# n = int(input("enter number of columns"))


# grid = []
# for i in range(m):
#     grid.append(list(input(f"Enter row {i}: ").split()))

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
max_area = 0
m, n = len(grid), len(grid[0])
print(m, n)
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
        return 0
    else:
        grid[i][j] = 0
        area = 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
    return area

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            max_area = max(max_area, dfs(i,j))
print(max_area)