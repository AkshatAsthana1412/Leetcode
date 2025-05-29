import math

# O(m*2^m)
# this approach starts at each element in the last row and tries
# to find the min sum path to the top of the triangle
# def min_sum(i, j, triangle):
#     if i == 0 and j == 0:
#         return triangle[i][j]
#     if i < 0 or j < 0 or i < j:
#         return math.inf
#     up = triangle[i][j] + min_sum(i-1, j, triangle)
#     diag = triangle[i][j] + min_sum(i-1, j-1, triangle)
#     return min(up, diag)

# Another solution is to start at the top of the triangle and find
# the min sum path to any bottom element
def min_sum(i, j, m, triangle):
    if i == m-1:
        return triangle[m-1][j]
    down = triangle[i][j] + min_sum(i+1, j, m, triangle)
    diag = triangle[i][j] + min_sum(i+1, j+1, m, triangle)
    return min(down, diag)

if __name__ == "__main__":
    m = int(input("Enter size of the triangle: "))
    grid = []
    for i in range(m):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        grid.append(row)
    # ans = math.inf
    # for k in range(m):
    #     res =  min_sum(m-1, k, grid)
    #     if res < ans:
    #         ans = res
    #     print(res)
    print(min_sum(0,0,m,grid))
