# https://leetcode.com/problems/132-pattern/


class Solution:
    
    # Runtime: 463 ms, faster than 49.42% of Python3 online submissions for 132 Pattern.
    # Memory Usage: 32.1 MB, less than 33.55% of Python3 online submissions for 132 Pattern.
    def find132pattern(self, nums) -> bool:
        stack = []
        secondmax = float("-inf")
        for i in range (len(nums)-1,-1,-1):
            
            if nums[i]< secondmax : 
                return True
            while stack and stack[-1]<nums[i]:
                secondmax = max(secondmax, stack.pop())
                
            stack.append(nums[i])
                
        return False
            
            