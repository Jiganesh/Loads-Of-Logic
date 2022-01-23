# https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution(object):
    
    # Runtime: 1484 ms, faster than 100.00% of Python online submissions for Rearrange Array Elements by Sign.
    # Memory Usage: 48 MB, less than 100.00% of Python online submissions for Rearrange Array Elements by Sign.
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        positive = [i for i in nums if i>=0]
        negative = [i for i in nums if i<0]
        array =[]
        for i in range(len(positive)):
            array.append(positive[i])
            array.append(negative[i])
        return array
    
    
    # Runtime: 2222 ms, faster than 100.00% of Python online submissions for Rearrange Array Elements by Sign.
    # Memory Usage: 44.2 MB, less than 100.00% of Python online submissions for Rearrange Array Elements by Sign.
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        positiveNumbers, negativeNumbers = [],[]
        while nums:
            [positiveNumbers, negativeNumbers][nums[-1]<0].append(nums.pop())
            
        n = len(positiveNumbers)
        while n:
            nums+= [positiveNumbers.pop(), negativeNumbers.pop()]
            n-=1
        return nums;