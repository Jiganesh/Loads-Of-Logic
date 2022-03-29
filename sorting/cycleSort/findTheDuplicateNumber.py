# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
# https://www.youtube.com/watch?v=dfIqLxAf-8s&ab_channel=TECHDOSE

class Solution(object):
    
    
    # Runtime: 768 ms, faster than 51.33% of Python online submissions for Find the Duplicate Number.
    # Memory Usage: 25.5 MB, less than 31.71% of Python online submissions for Find the Duplicate Number.
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums:
            i = abs(i)
            if nums[i] <0:
                return  i
            else :
                nums[i]*=-1
    
    # Runtime: 640 ms, faster than 72.90% of Python online submissions for Find the Duplicate Number.
    # Memory Usage: 25.4 MB, less than 40.35% of Python online submissions for Find the Duplicate Number.
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        while i < (len(nums)):
            if nums[i] != i+1:
                if nums[nums[i]-1] != nums[i]: nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else : return nums[i]
            else:
                i+=1
                
    # Runtime: 689 ms, faster than 64.13% of Python online submissions for Find the Duplicate Number.
    # Memory Usage: 25.2 MB, less than 79.08% of Python online submissions for Find the Duplicate Number.        
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow , fast = 0 , 0
        
        while True:
            
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast :
                print(slow)
                break
                
        slow2 = 0
        
        while True:
            
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow


    # Runtime: 1036 ms, faster than 17.21% of Python online submissions for Find the Duplicate Number.
    # Memory Usage: 25.3 MB, less than 40.35% of Python online submissions for Find the Duplicate Number.
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def countInArray(nums, num):
            count=0
            for i in nums:
                if i<=num:
                    count+=1
            return count
        
        low = 1 
        high = len(nums)-1
        
        # low and high is range not indices
        
        while low <= high:
            mid = low + (high -low)//2
            
            if countInArray(nums, mid) > mid : 
                # if the count of numbers which are less than mid is greater then that number is less than mid
                high = mid-1
            else :
                low = mid+1
                
        return low