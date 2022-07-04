# https://leetcode.com/problems/candy/
# REFERENCE :  PEAK AND VALLEYS Algorithm, Algoexpert video Array - Min Rewards


from typing import List
class Solution:
    
    # Runtime: 188 ms, faster than 80.59% of Python3 online submissions for Candy.
    # Memory Usage: 17.6 MB, less than 8.95% of Python3 online submissions for Candy.
    def candy(self, ratings: List[int]) -> int:
        
        
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        
        for i in range (1, len(ratings)):
            if  ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
                
        for i in range (len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
                
        result = [max(i) for i in list(zip(left, right))]
        
        return sum(result)