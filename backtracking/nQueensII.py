# https://leetcode.com/problems/n-queens-ii/

class Solution:
    
    # Runtime: 99 ms, faster than 33.15% of Python3 online submissions for N-Queens II.
    # Memory Usage: 13.8 MB, less than 98.68% of Python3 online submissions for N-Queens II.
    
    def totalNQueens(self, n: int) -> int:
        
        def DFS(queens, xy_dif , xy_sum):
            p = len(queens)
            if p == n:
                return 1
            
            ans = 0
            for q in range (n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    ans += DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
            return ans
        
        return DFS([],[],[])
        