# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        
        maximum_array = []
        maximum = 0
        for num in nums:
            maximum = max(num, maximum)
            maximum_array.append(maximum+num)
        result = list(accumulate(maximum_array, operator.add))
        return result
            