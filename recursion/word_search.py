# Check if the given 'word' exists in the board
# O(m*n*4^l)
from typing import List
class Solution:
    def search(self, i, j, board, word, p=0):
        # if we've reached the end of the word
        if p == len(word):
            return True
        # if invalid cell return false and end recursion tree
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[p]:
            return False
        # the only condition left is when board[i][j] == word[p], so no more checks needed
        temp = board[i][j]
        # mark board[i][j] as visited
        board[i][j] = ''
        # search in adjacent cells
        found = (self.search(i+1, j, board, word, p+1) or \
                 self.search(i-1, j, board, word, p+1) or \
                 self.search(i, j+1, board, word, p+1) or \
                 self.search(i, j-1, board, word, p+1))
        if found:
            return True
        else:
            # backtrack
            board[i][j] = temp
        return False
            

    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = self.search(i,j,word,board,0)
                    print(ans)
        return ans