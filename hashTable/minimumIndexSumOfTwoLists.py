# https://leetcode.com/problems/minimum-index-sum-of-two-lists/submissions/

class Solution:
    
    # TC : O(N^2)
    # SC : O(N)
    
    # Runtime: 374 ms, faster than 21.70% of Python3 online submissions for Minimum Index Sum of Two Lists.
    # Memory Usage: 14.5 MB, less than 41.03% of Python3 online submissions for Minimum Index Sum of Two Lists.
    
    # This solution has high memory footprint because of set and list.index does search in O(n)
    
    def findRestaurant(self, list1, list2):
        dictionary = { i : list1.index(i)+ list2.index(i) for i in set(list1)&set(list2)}
        return [x for x in dictionary if dictionary[x]== min(dictionary.values())]
    
    # Runtime: 200 ms, faster than 67.36% of Python3 online submissions for Minimum Index Sum of Two Lists.
    # Memory Usage: 14.4 MB, less than 86.75% of Python3 online submissions for Minimum Index Sum of Two Lists.
    
    # TC : O(N log N)
    # SC : O(N)
    def findRestaurant(self, list1, list2) :
        
        dictionary = {}
        
        for index , restaurant in enumerate(list1):
            if restaurant not in dictionary:
                dictionary[restaurant]=index
                
        minimum = float('inf')
        result = []
        
        for index, restaurant in enumerate(list2):
            if restaurant in dictionary :
                
                sumOfIndex = dictionary[restaurant]+index 
                
                if sumOfIndex < minimum:
                    result= [restaurant]
                    minimum=sumOfIndex    
                elif sumOfIndex == minimum:
                    result.append(restaurant)
                                
        return result
                
        
        
        