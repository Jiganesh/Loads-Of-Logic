# https://leetcode.com/problems/permutations-ii/
# Solution : https://www.youtube.com/watch?v=qhBVWf0YafA

class Solution(object):
    
    # Submitted by @Jiganesh
    # Runtime: 48 ms, faster than 80.65% of Python online submissions for Permutations II.
    # Memory Usage: 13.8 MB, less than 43.75% of Python online submissions for Permutations II.
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        permutations =[]
        
        countDictionary = {i:nums.count(i) for i in nums}
        
        def dfs ():
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return 
            
            for n in countDictionary:
                if countDictionary[n]>0:
                    countDictionary[n] -= 1
                    permutations.append(n)
                    
                    dfs()
                    countDictionary[n] += 1
                    permutations.pop()
        dfs()
        
        return result
    
print(Solution().permuteUnique([1,1,2]))
        