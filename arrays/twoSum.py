// https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

    # Brute Force:

    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]





    # Improved :
    # if difference exists in list, return current index and that numbers index

    # for i in range(len(nums)):
    #     if target-nums[i] in nums[i+1:]:
    #         return [i, nums[i+1:].index(target-nums[i])+i+1]





     # Better Approach:

     # Runtime: 48 ms, faster than 99.11% of Python3 online submissions for Two Sum.
     # Memory Usage: 15.5 MB, less than 12.63% of Python3 online submissions for Two Sum.

     # create a dictionary/map to create key value pair
     # for key-(target-first number ie (expected 2nd num)) value-(first number's index)
     # So when second number occurs (which is target-first number) we can check in map & get first number's index
     # and return 1st index and current index(2nd number's index)

    mapp = {}
    for i in range(len(nums)):
        if nums[i] in mapp:
            return (mapp[nums[i]], i)
        else:
            mapp[target - nums[i]] = i


# input:
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
