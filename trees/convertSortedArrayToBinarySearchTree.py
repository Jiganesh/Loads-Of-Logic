# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Runtime: 123 ms, faster than 44.73% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Memory Usage: 15.6 MB, less than 35.48% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST(self, nums) :
        
        def helper (nums):
            if nums ==[]:
                return None
            else:
                mid = len(nums)//2
                root = TreeNode( nums[mid])
                root.left = helper(nums[:mid])
                root.right = helper(nums[mid+1: ])
                
            return root
        
        return helper(nums)
            