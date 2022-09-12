# https://leetcode.com/problems/most-frequent-subtree-sum/

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Runtime: 66 ms, faster than 72.28% of Python3 online submissions for Most Frequent Subtree Sum.
    # Memory Usage: 17.9 MB, less than 11.80% of Python3 online submissions for Most Frequent Subtree Sum.
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        lookup = defaultdict(lambda :[0,0])
        self.max_count = 0
        
        def helper(root, click):
            if root:
                
                left = helper(root.left, click+2) 
                right = helper(root.right, click+1)
                
                value_at_node = root.val + left + right

                count_of_value_at_node = lookup[value_at_node][0]

                self.max_count = max(self.max_count, count_of_value_at_node +1)
                
                lookup[value_at_node] =  (count_of_value_at_node+1, click+1) 
                
                return value_at_node

            return 0
                
        helper(root,0)
        result = sorted([i for i in lookup if lookup[i][0]== self.max_count], key = lambda x : -lookup[x][1])
        return result 