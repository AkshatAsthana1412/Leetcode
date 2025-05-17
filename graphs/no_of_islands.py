# m = int(input("Enter number of rows"))
# n = int(input("enter number of columns"))


# grid = []
# for i in range(m):
#     grid.append(list(input(f"Enter row {i}: ").split()))

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

m = len(grid)
n = len(grid[0])

def dfs(i,j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
        return
    else:
        grid[i][j] = 0
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i,j+1)
        dfs(i, j-1)

cnt = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] ==1:
            cnt += 1
            dfs(i, j)
print(cnt)

