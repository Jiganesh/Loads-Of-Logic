# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        self.total = 0
        def helper(node):
            if node >= n :
                return 0
            
            left= helper(2*node +1)
            right = helper(2*node +2)
            
            self.total += abs(left-right)
            return max(left,right) + cost[node]
        helper(0)
        return self.total