# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution(object):
    
    # TC :O(N^2)
    # SC : O(N)
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = [1]*(len(nums));
        
        for i in range(len(nums)):
            currentNum = nums[i]
            for j in range(0, i):
                otherNum = nums[j]
                if (otherNum<currentNum and length[j]+1>= length[i]):
                    length[i]=length[j]+1
        print(nums, length)
        return max(length)

# TestCases

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7]))
print(Solution().lengthOfLIS([4,10,4,3,8,9]))
print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
