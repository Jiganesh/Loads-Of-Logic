import bisect, heapq, operator, math
from typing import List, Optional
from itertools import accumulate
from collections import defaultdict, Counter, deque
from functools import lru_cache, cmp_to_key


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1


def make_tree (array , i , n):
    
    root = None
    if i < n:
        
        root = TreeNode(array[i])
        left_node = make_tree(array, 2*i+1, n)
        right_node = make_tree(array, 2*i+2, n)
        
        root.left = left_node
        root.right = right_node
        
    return root
    
array= [10,5,-3,3,2,None,11,3,-2,None,1]
root = make_tree(array, 0, len(array))
print(Solution().pathSum(root , 8))
