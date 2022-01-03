
class Solution(object):
    def shuffle(self, nums, n):

        #List Slicing
        #Max with this
        # Runtime: 52 ms, faster than 96.86% of Python3 online submissions for Shuffle the Array.
        # Memory Usage: 14.2 MB, less than 92.90% of Python3 online submissions for Shuffle the Array.
        
        neww=[]
        new1=nums[:n]
        new2=nums[n:]
        for i in range(n):
            neww.append(new1[i])
            neww.append(new2[i])
        return neww
        
        

        #Runtime: 52 ms, faster than 96.86% of Python3 online submissions for Shuffle the Array.
        #Memory Usage: 14.3 MB, less than 78.23% of Python3 online submissions for Shuffle the Array.

#         arr=[]
#         for i in range(n):
#            arr.append(nums[i])
#            arr.append(nums[i+n])
#         return arr
        
    
        #two pointer
        
        # p1,p2,neww=0,n,[]
        # while(p1<n):
        #     neww.append(nums[p1])
        #     neww.append(nums[p2])
        #     p1+=1
        #     p2+=1
        # return neww
    
    
    
        # One liner solution
        # return [j for i in range(n) for j in (nums[i], nums[i+n])]
    
        ''' One liner Explanation'''
        
        '''
        
        for i in range(n):
            for j in (nums[i], nums[i+n]):
                print(j)
        '''
    
    

    
print(Solution.shuffle(Solution, [2,5,1,3,4,7], 3))
    
