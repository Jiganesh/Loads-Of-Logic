from collections import Counter
def numIdenticalPairs(nums):
    
    #1 Brute force 
    
    # count=0
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i]==nums[j]:
    #             count+=1
    # return count
    
    
    
    
    #2 with count removing other for loop
    
    # pairs=0
    # for i in set(nums):
    #     x=nums.count(i)
    #     pairs+=(x*(x-1))//2
    # return pairs
    
    
    


    #3 improved with dictionary form and list comprehension
    
    #Dictionary with Count for improved efficiency 
    # mapp={i:nums.count(i) for i in set(nums)}
    
    #OR with counter from collections
    # mapp=Counter(nums) 
    
    # return sum([(x*(x-1))//2 for x in mapp.values()])
    
    
    
    
    
    #4 with lambda 
    cal= lambda x : (x*(x-1))//2
    return sum(cal(a) for a in Counter(nums).values())

#input
nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))