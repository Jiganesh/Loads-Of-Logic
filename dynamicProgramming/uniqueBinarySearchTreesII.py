# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def helper(nums):
            

            if not nums:
                return [None]

            result = []

            for ind in range (len(nums)):
                left = helper(nums[:ind])
                right = helper(nums[ind+1:])

                for l in left:
                    for r in right:
                        root = TreeNode(nums[ind])
                        root.left = l
                        root.right = r
                        result.append(root)
            return result

        nums = [i for  i in range(1, n+1)]
        return helper(nums)
