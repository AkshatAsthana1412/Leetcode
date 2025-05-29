from typing import List
class Solution:
    def get_combs(self, i, j, comb, ans=[]):
        if i == 0 and j == 0:
            ans.append(''.join(comb.copy()))
            return
        
        if i > 0:
            comb.append('(')
            self.get_combs(i-1, j, comb, ans)
            comb.pop()
        
        if j > i:
            comb.append(')')
            self.get_combs(i, j-1, comb, ans)
            comb.pop()

        return ans
    def generateParenthesis(self, n: int) -> List[str]:
        return self.get_combs(n, n, [], [])