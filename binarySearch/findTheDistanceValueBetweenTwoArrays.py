import bisect

class Solution:
    # TC : O(N*M)
    # SC : O(1)
    
    # Runtime: 159 ms, faster than 35.54% of Python3 online submissions for Find the Distance Value Between Two Arrays.
    # Memory Usage: 13.9 MB, less than 98.47% of Python3 online submissions for Find the Distance Value Between Two Arrays.
    def findTheDistanceValue(self, arr1, arr2, d) -> int:
        
        count = 0
        for i in arr1: 
            for j in arr2:
                if abs(i-j) <=d:
                    break
            else:
                count+=1
        
        return count
    
    
    # TC : O(N log M)
    # SC : O(1)
    
    # Runtime: 133 ms, faster than 50.92% of Python3 online submissions for Find the Distance Value Between Two Arrays.
    # Memory Usage: 13.9 MB, less than 78.54% of Python3 online submissions for Find the Distance Value Between Two Arrays.   
    def findTheDistanceValue(self, arr1, arr2, d) -> int:
        count=0
        arr2.sort()
        
        for i in arr1:
            
            left = bisect.bisect_left(arr2, i-d)
            right = bisect.bisect_right(arr2, i+d)
            
            if left==right:
                count+=1
        
        return count