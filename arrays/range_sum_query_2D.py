from typing import List
# Find the sum of the submatrix with corners: [(row1, col1), (row2, col2)] (used prefix sum to optimise)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.mem = [[0]*n for _ in range(m)]
        self.initialise_mem(m, n)
    
    def initialise_mem(self, m:int, n:int):
        for i in range(m):
            for j in range(n):
                self.prefix_sum(i, j)
        return self

    def prefix_sum(self, r:int, c:int) -> int:
        s = 0
        if r == 0 and c == 0:
            s = self.matrix[r][c]
        elif r > 0 and c > 0:
            s = self.mem[r-1][c] + self.mem[r][c-1] + self.matrix[r][c] - self.mem[r-1][c-1]
        elif r - 1 < 0:
            s = self.mem[r][c-1] + self.matrix[r][c]
        elif c - 1 < 0:
            s = self.mem[r-1][c] + self.matrix[r][c]
        else:
            for p in range(r+1):
                for q in range(c+1):
                    s += self.matrix[p][q]
        self.mem[r][c] = s
        return s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.mem[row2][col2]
        if row1 - 1 < 0 or col1 - 1 < 0:
            d = 0
        else:
            d = self.mem[row1-1][col1-1]
        if row1 - 1 < 0:
            b = 0
        else:
            b = self.mem[row1-1][col2]
        if col1 - 1 < 0:
            c = 0
        else:
            c = self.mem[row2][col1-1]
        return a - b - c + d


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)