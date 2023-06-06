# https://leetcode.com/problems/majority-element-ii/
# https://www.youtube.com/watch?v=yDbkQd9t2ig


from collections import Counter
from typing import List

class Solution:
    
    # Naive Approach
    
    # TC : O(N)
    # SC : O(N)
    def majorityElement(self, nums: List[int]) -> List[int]:

        lookup = Counter(nums)
        return [i for i in lookup if lookup[i] > len(nums)//3]
    
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num1, count1 = float("-inf"), 0
        num2, count2 = float("-inf"), 0

        for num in nums:
            
            if num1 == num:
                count1 += 1
            elif num2 == num:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 ==0:
                num2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1

        result = []
        k = len(nums)//3

        count1 , count2 = 0, 0
        for num in nums:
            if num == num1:
                count1+=1
            if num == num2:
                count2+=1

        if count1 > k:
            result.append(num1)
        if count2 > k :
            result.append(num2)

        return result
        
    