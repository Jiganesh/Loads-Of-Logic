# https://leetcode.com/problems/path-sum-ii/


from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Runtime: 74 ms, faster than 38.88% of Python3 online submissions for Path Sum II.
    # Memory Usage: 19.2 MB, less than 14.15% of Python3 online submissions for Path Sum II.
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.result  = []
        def helper(root, currentSum = 0, array = []):
            
            if root:
                
                if not root.left and not root.right and  root.val+currentSum == targetSum :
                    self.result.append(array[:]+[root.val])
                else:
                    helper(root.left, currentSum+root.val, array+[root.val])
                    helper(root.right, currentSum+root.val, array+[root.val])
                    
        
        helper(root)
        return self.result