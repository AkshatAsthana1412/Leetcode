mat = [[2,2,2],
       [2,2,2],
       [2,2,2]]

m, n = len(mat), len(mat[0])
tg_c = 2
sr, sc = (2, 0)
c = mat[sr][sc]
if c == tg_c:
    print(mat) # end here
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or mat[i][j] != c:
        return
    mat[i][j] = tg_c
    for node in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        dfs(node[0], node[1])

dfs(sr, sc)
print(mat)
