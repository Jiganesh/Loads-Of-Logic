# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution(object):
    
    
    # Submitted by Jiganesh
    
    # TC : O(N^2) 1561 ms
    # SC : O(1)   13.6 MB
    
    class Solution(object):
        def findKDistantIndices(self, nums, key, k):
            """
            :type nums: List[int]
            :type key: int
            :type k: int
            :rtype: List[int]
            """
            
            result = set()
            
            for i in range(len(nums)):
                for j in range(len (nums)):
                    if abs(i-j)<=k and nums[j]==key:
                        result.add(i)
                        
            return sorted(result)
    
    # TC : O(N*K)  621 ms
    # SC : O(K)   39 MB
    
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        
        arr = [i for i in range (len(nums)) if nums[i]==key]
        
        result = set()
        for i in range(len(nums)):
            for j in arr:
                if abs(i-j)<=k :
                    result.add(i)
                    
        return sorted(result)
    
    # Most Optimal Solution
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 52 ms, faster than 97.02% of Python online submissions for Find All K-Distant Indices in an Array.
    # Memory Usage: 13.6 MB, less than 65.58% of Python online submissions for Find All K-Distant Indices in an Array.

    
    def findKDistantIndices(self, nums, key, k):
        
        
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        result = []
        start , end = 0,0
        
        for pointerToSearchKey in range(len(nums)):
            
            if nums[pointerToSearchKey] == key :
                
                
                if len(result)==0:
                    start = 0
                else :
                    start = result[-1]+1
                    
                
                start = max(pointerToSearchKey-k, start)
                end = min(pointerToSearchKey+k, len(nums)-1)
                                
                for indicesInVicinity in range (start, end+1):
                    result.append(indicesInVicinity)
                    
        return result
    



