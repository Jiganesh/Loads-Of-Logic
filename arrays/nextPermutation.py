#https://leetcode.com/problems/next-permutation/

def nextPermutation(nums):
    """
    IMP: Do not return anything, modify nums in-place instead.
    """
    
    #so my approach was to getting all the permutations of nums and
    #to get those in lexicographical order lst.sort(key=str)
    #set is used to remove duplicats and increase efficiency
    #now if element is at last ie pure desc then replace nums with first value which is asc
    #else give next lexicographical output
    
    # perms=list(i for i in set(permutations(nums)))
    # perms.sort(key=str)
    # if tuple(nums)==perms[-1]:
    #     nums[:]=perms[0]
    # else:
    #     m=perms.index(tuple(nums))
    #     nums[:]=perms[m+1]
            
    #but this was naive approach as getting all permutations is very costly n! so got TLE :(
    
    
    #Time: O(n) and space: O(1)
    #now we need to find out non-increasing value pivot ie value upto which right side values are decreasing
    #this will be tracked by i
    #and then with that pivot find its next larger value from right to swap it
    #this will be tracked by j
    #and we will swap those values and from that pivot we will reverse right side values with list slicing
    #refered to https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


    i=j=len(nums)-1
    while i>0  and  nums[i-1]>=nums[i]:
        i-=1
    #if all values are decreasing i will become 0 
    #in that case we will just reverse the list
    if i==0:
        nums.reverse()
        return
    #else we will find j and swap it
    #now our pivot is the left element of i as while loop break out at i not pivot
    while nums[j]<=nums[i-1]:
        j-=1
        
    nums[j], nums[i-1]=nums[i-1], nums[j]
    
    nums[i:]= nums[len(nums)-1: i-1:-1]

    #for our local o/p we will return nums
    return nums
print(nextPermutation([1,2,3]))
print(nextPermutation([1,1,5]))