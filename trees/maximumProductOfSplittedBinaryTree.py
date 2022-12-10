# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        self.total =  0
        def helper(root):
            if root:
                helper(root.left)
                self.total += root.val
                helper(root.right)

        helper(root)
        print(self.total)


        self.result = 0

        def find_split(root):

            if root:
                
                left = find_split(root.left)
                right = find_split(root.right)

                sum1 = root.val+left+right
                self.result = max((self.total-sum1) * sum1, self.result)
                return sum1

            return 0

        find_split(root)
        return self.result% MOD
