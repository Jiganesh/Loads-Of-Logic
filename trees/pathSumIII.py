# https://leetcode.com/problems/path-sum-iii/
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)


from typing import List, Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Runtime: 1073 ms, faster than 16.40% of Python3 online submissions for Path Sum III.
    # Memory Usage: 15.2 MB, less than 78.04% of Python3 online submissions for Path Sum III.
    
    
    # TC: Skewed Tree O(N^2) and Balanced Tree O(NlogN)
    # SC : Skewed Tree O(N) and Balanced Tree O(Log N)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def helper(root, currentSum=0):    
            if not root: return 0
            
            return  ((root.val+currentSum ) == targetSum) + helper(root.left,  currentSum+root.val)  + helper(root.right, currentSum+root.val)
            
            
        def parent_helper(root):
            if not root : return 0
            
            root_sum = helper(root)
            left = parent_helper(root.left) if root.left else 0
            right = parent_helper(root.right) if root.right else 0
            
            return root_sum + left + right
        
        
        return parent_helper(root)

    # TC : Skewed Tree O(N) and  Balanced Tree O(logN)
    # SC : Skewed Tree O(N) and Balanced Tree O(logN)
    
    # Runtime: 65 ms, faster than 84.08% of Python3 online submissions for Path Sum III.
    # Memory Usage: 15.4 MB, less than 31.22% of Python3 online submissions for Path Sum III.
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.result = 0
        def helper(root, current_path_sum, target , cache):
            
            if not root : return 0
            
            current_path_sum = root.val + current_path_sum
            old_path_sum = current_path_sum - target
            
            self.result += cache[old_path_sum]
            cache[current_path_sum]+=1
            
            
            helper(root.left , current_path_sum, target, cache)
            helper(root.right , current_path_sum, target, cache)
            
            cache[current_path_sum]-=1
            
        cache = defaultdict(int)
        cache[0] = 1
        
        helper(root, 0 , targetSum, cache)
        
        return self.result
            
            