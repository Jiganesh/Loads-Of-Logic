# https://leetcode.com/problems/search-suggestions-system/

class Solution:
        
    # Runtime: 553 ms, faster than 30.65% of Python3 online submissions for Search Suggestions System.    
    # Memory Usage: 16.9 MB, less than 99.69% of Python3 online submissions for Search Suggestions System.    
        
        
    # TC : O(N log N + N^2)
    # SC : O(N)
    def suggestedProducts(self, products, searchWord) :
        
        result = []
        products.sort()
        
        for i in range(1,len (searchWord)+1):
            string = searchWord[:i]
            result.append([i for i in products if i.startswith(string)][:3])
            
        return result 
            
            
            