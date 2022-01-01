#https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):
    l=len(nums)
    #1
    return [nums[nums[i]] for i in range(l)]
    
    #2
    return [nums[i] for i in nums]