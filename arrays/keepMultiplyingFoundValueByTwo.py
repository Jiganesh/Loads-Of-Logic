class Solution(object):
    
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
        # We will sort the array to not miss out any higher values which came first
        nums.sort()
        
        # We will traverse the sorted array and multiply the number by 2
        for i in nums:
            if i== original:
                original*=2
                
        return original
    
print(Solution().findFinalValue([5,3,6,1,12],3))
print(Solution().findFinalValue([2,7,9],4))

        