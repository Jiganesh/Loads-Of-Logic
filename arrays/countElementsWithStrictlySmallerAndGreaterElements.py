# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution(object):
    
    # Runtime: 16 ms, faster than 100.00% of Python online submissions for Count Elements With Strictly Smaller and Greater Elements .
    # Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Count Elements With Strictly Smaller and Greater Elements .   
    
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minimum = min(nums)
        maximum = max(nums)
        
        
        count =0;
        for i in  nums:
            if i>minimum and i< maximum:
                count+=1
        return count
    
print(Solution().countElements([11,7,2,15]))
print(Solution().countElements([-3,3,3,90]))
