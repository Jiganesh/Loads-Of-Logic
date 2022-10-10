# Solution : https://www.youtube.com/watch?v=QRa9ZVGMWlY
# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    
    TC : O(N)
    SC : O(N)
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n, k):

            if n==1:
                return 0

            parent = helper(n-1, k//2)

            if parent == 1:
                return 0 if k&1 else  1
            else:
                return 1 if k&1 else  0

        return helper(n, k-1)
