# Question : https://leetcode.com/problems/binary-tree-right-side-view/
# Solution : https://www.youtube.com/watch?v=KV4mRzTjlAk&ab_channel=takeUforward

class Solution(object):
    
    # TC : O(N)
    # SC : O(H)
    
    # Runtime: 47 ms, faster than 5.05% of Python online submissions for Binary Tree Right Side View.
    # Memory Usage: 13.6 MB, less than 25.43% of Python online submissions for Binary Tree Right Side View.
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def helper(arr, root, level):
            if root:
                if level >= len(arr):
                    arr.append(root.val)
                    
                helper(arr, root.right, level+1)
                helper(arr, root.left, level+1)
                
            return arr
        
        array , level =[], 0
        return helper(array, root, level)