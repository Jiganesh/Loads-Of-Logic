class Solution(object):
    
    
    # TC : O(N)
    #  SC: O(N)
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)+1
        
        indexcount = [0]*a
        exclude = [0]*a
        include = [0]*a
        
        for i in nums:
            indexcount[i]+=1
            
        for i in range(1,a):
            exclude[i] = max(include[i-1], exclude[i-1])
            include [i]= i*indexcount[i]+ exclude[i-1]
          
        #print(exclude)
        #print(include)
        
        return max(exclude[-1], include[-1])