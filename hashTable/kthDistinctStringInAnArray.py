# https://leetcode.com/problems/kth-distinct-string-in-an-array/


from collections import Counter

class Solution:
    
    # Runtime: 63 ms, faster than 98.24% of Python3 online submissions for Kth Distinct String in an Array.
    # Memory Usage: 14 MB, less than 94.46% of Python3 online submissions for Kth Distinct String in an Array.
    def kthDistinct(self, arr, k: int) -> str:
        
        dictionary = Counter(arr)
        
        for i in arr:
            if k==1 and dictionary[i]==1:
                return i
            
            if dictionary[i]==1:
                k-=1
        
        return ""
        