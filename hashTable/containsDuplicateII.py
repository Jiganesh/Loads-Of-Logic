# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    
    # Runtime: 720 ms, faster than 65.63% of Python3 online submissions for Contains Duplicate II.
    # Memory Usage: 32.1 MB, less than 9.33% of Python3 online submissions for Contains Duplicate II.
    
    def containsNearbyDuplicate(self, nums,k) -> bool:
        
        dictionary = {}
        
        for i in range (len(nums)):
            if nums[i] in dictionary :
                dictionary[nums[i]].append(i)
            else :
                dictionary[nums[i]] =[i]        
        
        for i in dictionary :
            if len(dictionary[i]) >1:
                for j in range (len(dictionary[i])-1):
                    
                    if abs(dictionary[i][j+1]-dictionary[i][j]) <=k:
                        return True
        return False
    
    # Above Solution Optimized
    
    # Runtime: 632 ms, faster than 89.52% of Python3 online submissions for Contains Duplicate II.
    # Memory Usage: 27.3 MB, less than 23.83% of Python3 online submissions for Contains Duplicate II.
                    
    def containsNearbyDuplicate(self, nums, k) -> bool:
        
        dictionary = {}
        for i in range (len(nums)):
            if nums[i] in dictionary and abs(dictionary[nums[i]]-i) <=k:
                dictionary[nums[i]]=i
                return True
            else :
                dictionary[nums[i]] = i
        return False
    
    # Same as Above but Aesthetic Code
    def containsNearbyDuplicate(self, nums, k) -> bool:
        dictionary = {}
        
        for i in range (len(nums)):
            if nums[i] in dictionary and abs(dictionary[nums[i]]-i) <=k:
                return True
            dictionary[nums[i]] = i
        return False
    
    
    # Rolling Window Approach (IMP)
    def containsNearbyDuplicate(self, nums, k) -> bool:
        rolling_window = set()
        for idx, num in enumerate(nums):
            if idx > k:
                rolling_window.remove(nums[idx-k-1])
            if num in rolling_window:
                return True
            rolling_window.add(num)
        return False
    
    
print(Solution().containsNearbyDuplicate([1,2,3,1]))
    
    