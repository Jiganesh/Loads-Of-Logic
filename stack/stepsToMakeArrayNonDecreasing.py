# https://leetcode.com/problems/steps-to-make-array-non-decreasing/
class Node : 
    def __init__(self, key , value):
        self.key = key 
        self.value = value
          
class Solution(object):
    
    # Runtime: 1091 ms, faster than 50.00% of Python online submissions for Steps to Make Array Non-decreasing.
    # Memory Usage: 61.4 MB, less than 50.00% of Python online submissions for Steps to Make Array Non-decreasing.
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack  =[]
        maximum = 0
        
        for i in range (len(nums)-1, -1,-1):
            
            count = 0
            while stack and stack[-1].key <nums[i]:
                count = max (count+1,stack[-1].value )
                stack.pop()
            stack.append(Node(nums[i], count))
            maximum = max(count, maximum)
            
        return maximum
            
        
        