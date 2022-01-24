# https://leetcode.com/problems/can-place-flowers/

class Solution(object):
    
    
    # Submitted by @ Jiganesh
    # TC: O(N)
    # SC : O(N)
    
    # Runtime: 210 ms, faster than 23.37% of Python online submissions for Can Place Flowers.
    # Memory Usage: 13.8 MB, less than 75.18% of Python online submissions for Can Place Flowers.
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        flowerbed=[0]+flowerbed+[0]
        
        i=1
        while (i < len(flowerbed)-1 and n):
            if flowerbed[i]==0 and flowerbed[i-1] ==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            i+=1
        return n==0
    
    # Submitted by @ Jiganesh
    # TC: O(N)
    # SC : O(1)
    
    # Runtime: 203 ms, faster than 26.45% of Python online submissions for Can Place Flowers.
    # Memory Usage: 13.6 MB, less than 93.12% of Python online submissions for Can Place Flowers.
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        i=0
        while (i < len(flowerbed)and n):
            
            if flowerbed[i]==0:
                
                prevSpace = 0 if i==0 or flowerbed[i-1]==0 else 1
                nextSpace = 0 if i==len(flowerbed)-1 or flowerbed[i+1]==0 else 1
                
                if prevSpace==0 and nextSpace==0:
                    flowerbed[i]=1
                    n-=1
            i+=1
        return n==0