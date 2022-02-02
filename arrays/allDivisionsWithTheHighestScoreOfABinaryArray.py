class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC: O(N)
    # SC : O(N)
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countOne = 0
        for i in nums:
            if i ==1 :
                countOne+=1
        countZero =0
        
        # At Initial left = 0 and right = countOne hence countOne will be initial value
        
        
        maximum =[countOne] 
        
        # # For Example:
        # Input: nums = [0,0,1,0]
        # Output: [2,4]
        
        # - 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.     # This will be initial value
        # - 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
        # - 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
        # - 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
        # - 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
        
        
        for i in range (len(nums)):
            # We just keep the track of number of 1's and 0's we have 
            # manipulate them when traversing the array
            
            if nums[i]==0:
                # if we find the number is zero then it will be added in left
                # hence we increase the countZero by 1 as new 0 was added in left
                countZero +=1
            elif nums[i]==1:
                # if we find the number is one the we know it is removed from right 
                # hence we will decrement the countOne by 1 as new 1 was removed from right
                countOne -=1
                
            maximum.append(countZero+countOne)
            
        maxi  =max(maximum)
        return [ i for i in range(len(maximum)) if maximum[i]==maxi]
    