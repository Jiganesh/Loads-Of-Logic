# https://leetcode.com/problems/subsets-ii/
# https://www.youtube.com/watch?v=u40eYbmT9zg


# If not understood the pro approach try book and pen 
from typing import List

class Solution:
    
    # Naive Approach
    # TC : O(N*2^N)
    # SC : O(N^2)
    
    
    #Naive Approach
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        result = set()
        result.add(tuple([]))
        nums.sort()
        n = len(nums)

        def helper(index, array ):

            for ind in range(index+1, n ):
                array.append(nums[ind])
                result.add(tuple(array))
                helper(ind, array)
                array.pop()

        helper(-1, [])
        return result


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        result = [[]]
        current = []

        n = len(nums)
        for ind in range (n):
            if ind > 0 and nums[ind] == nums[ind-1]:
                current = [item + [nums[ind]] for item in current]
            else:
                current = [item + [nums[ind]] for item in result]
            result += current 
        
        return result 
