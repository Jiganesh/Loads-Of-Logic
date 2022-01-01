#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ 

def twoSum2(numbers, target):
    
    #Dictionary/Map solution:
    #O(n) ( O(n): for loop + "in map" O(1) )
    # mapp={}
    # for i in range(len(numbers)):
    #     if numbers[i] in mapp:
    #         return (mapp[numbers[i]]+1, i+1)
    #     else:
    #         mapp[target-numbers[i]]=i
    
    
    
    #Two pointer Solution:
    #take 2 pointers as indexes and if sum is less or greater than target
    #adjust pointers according to it.
    #O(n)
    
    l,r=0, len(numbers)-1
    while (l<r):
        summ=numbers[l]+numbers[r]
        if summ==target:
            return (l+1, r+1)
        elif (summ<target):
            l+=1
        else:
            r-=1
        
        
    #Binary Search Solution:
    #for each number take expected 2nd number and find it using binary search as list is already sorted
    #O(nlogn)
    
    # for i in range(len(numbers)):
    #     #to make sure it handles duplicates, l=i+1
    #     l,r=i+1, len(numbers)-1
    #     other=target-numbers[i]
    #     while l<=r:
    #         mid=l+(r-l)//2
    #         if numbers[mid]==other:
    #             return (i+1,mid+1)
    #         elif numbers[mid]<other:
    #             l=mid+1
    #         else:
    #             r=mid-1




#Input
numbers = [2,7,11,15]
target = 9
print(twoSum2(numbers, target))