# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
# https://www.youtube.com/watch?v=h9t7JF50Mpw 

from typing import List

class Solution:

    # TC : O(N)
    # SC : O(N)

    # Runtime: 2346 ms, faster than 23.74% of Python3 online submissions for Minimum Deletions to Make Array Beautiful.
    # Memory Usage: 28.1 MB, less than 85.98% of Python3 online submissions for Minimum Deletions to Make Array Beautiful.
    def minDeletion(self, nums: List[int]) -> int:
        
        stack = []
        n = len(nums)
        stack_index = 0
        
        for i in nums:
            
            if stack and stack_index&1 and stack[-1] == i:
                continue  
            
            stack.append(i)
            stack_index+=1
            

        s = len(stack)
        s = s if s%2==0 else s-1
        return n-s
    
    # TC : O(N
    # SC : O(1)
    
    # Runtime: 2041 ms, faster than 44.30% of Python3 online submissions for Minimum Deletions to Make Array Beautiful.
    # Memory Usage: 28 MB, less than 90.65% of Python3 online submissions for Minimum Deletions to Make Array Beautiful.
    def minDeletion(self, nums: List[int]) -> int:
        
        d = 0
        
        for i in range (len(nums)-1):
            if (i-d)%2==0 and nums[i] == nums[i+1]:
                d+=1
                
        n = len(nums)-d   # checking how many left in array
        
        # if elements left in array are even return d or else do one more deletion
        return d if n%2==0 else d+1

print(Solution().minDeletion([1,1,2,2,3,3]))
print(Solution().minDeletion([1,1,2,3,5]))