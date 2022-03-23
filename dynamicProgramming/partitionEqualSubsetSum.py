# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    
    # TLE
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summation = sum(nums)
        
        subsets = [[]]
        for num in nums:
            subsets+= [i+[num] for i in subsets]
                    
            
        for i in subsets:
            s= sum(i)
            if s==summation-s:
                return True
        
        return False
    
    # Top Down Approach
    
    # Runtime: 3828 ms, faster than 11.33% of Python online submissions for Partition Equal Subset Sum.
    # Memory Usage: 35.4 MB, less than 11.71% of Python online submissions for Partition Equal Subset Sum.
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summation = sum(nums)
        
        def subsetSum (arr, sum):
            
            dp =  [ [0 for i in range(sum+1)] for i in range(len(arr)+1)]
            
            
            for i in range (len(arr)+1):
                for j in range(sum+1):
                    if i==0:
                        dp[i][j] = False
                    elif j==0:
                        dp[i][j] = True
                    elif arr[i-1]<=j:
                        dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[len(arr)][sum]
        
        if summation%2 ==0:
            return subsetSum(nums, summation//2)
        
        return False
    
    # using memoization
    
    
    # Runtime: 48 ms, faster than 98.46% of Python online submissions for Partition Equal Subset Sum.
    # Memory Usage: 14.1 MB, less than 70.40% of Python online submissions for Partition Equal Subset Sum.
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = {0:True}
        def dfs(index, remainder):
            if remainder in dp:
                return dp[remainder]
            dp[remainder] = False
            if remainder > 0:
                for i in range(index,  len(nums)):
                    if dfs(i+1, remainder - nums[i]):
                        dp[remainder] = True
                        break
            return dp[remainder]
        
        s = sum(nums)
        if s%2 != 0: return False
        return dfs(0, s//2)
            
        