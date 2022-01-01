#https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums):
    #1:
    
    # summ,op=0,[]
    # for i in range(len(nums)):
    #     summ+=nums[i]
    #     op.append(summ)
    # return op
    
    #2:
    
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    return nums
    
    #3:
    
    # return [sum(nums[:i+1]) for i in range(len(nums))]

#input:
nums = [1,2,3,4]
print(runningSum(nums))