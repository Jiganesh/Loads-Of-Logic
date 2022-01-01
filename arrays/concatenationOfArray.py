#https://leetcode.com/problems/concatenation-of-array/

def getConcatenation(nums):
    #1: brute force
    # for i in range(len(nums)):
    #     nums.append(nums[i])
    # return nums
    
    #2: concatenate
    return nums+nums

    #3: using extend
    # nums.extend(nums)
    # return nums

    #4: list comprehension
    # return [i for x in range(2) for i in nums]
    
    #5: unpaking list items
    # return [*nums]*2

#input
nums = [1,2,1]
print(getConcatenation(nums))