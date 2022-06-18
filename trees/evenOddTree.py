# https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 762 ms, faster than 49.31% of Python3 online submissions for Even Odd Tree.
    # Memory Usage: 41 MB, less than 39.06% of Python3 online submissions for Even Odd Tree.
    
    def isEvenOddTree(self, root) -> bool:
        
        def is_even_and_decreasing(array):
            
            if len([i for i in array if i&1])>0 : return False

            for i in range (1, len(array)):    
                if array[i-1]%2!=0 or array[i]%2!=0 or array[i-1]<=array[i]:
                    return False
            return True
                    
        def is_odd_and_increasing(array):
            if len([i for i in array if i%2==0])>0 : return False
            
            for i in range (1,len(array)):
                if  (array[i]%2==0) or (array[i-1]%2==0) or (array[i-1] >= array[i]):
                    return False
            return True
        
        def check(level, array):            
            if level%2==0:
                return is_odd_and_increasing(array)
            else:
                return is_even_and_decreasing(array)
                
        level = 0
        q = [root]
        
        while q:
            array = [i.val for i in q]
            if check(level, array)==False:
                # print(level, array)
                return False
            q = [child for p in q for child in [p.left, p.right] if child]
            level+=1
        return True
            
                
            
            
            
        
        