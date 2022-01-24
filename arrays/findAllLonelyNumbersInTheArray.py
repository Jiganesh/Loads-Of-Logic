# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
# Solution : https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/discuss/1711243/Python-Counter
from matplotlib import collections


class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 1757 ms, faster than 100.00% of Python online submissions for Find All Lonely Numbers in the Array.
    # Memory Usage: 40.9 MB, less than 100.00% of Python online submissions for Find All Lonely Numbers in the Array.
    
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        
        for i in nums :
            if i in dictionary:
                dictionary[i]=dictionary[i]+1
            else :
                dictionary[i]=1
   
        array =[]
        for i in nums :
            if i-1 not in dictionary and i+1 not in dictionary and dictionary[i]==1:
                array.append(i)
        return array
    
    
    # TC : O(N)
    # SC : O(N)

    def findLonely(self, nums):
        count = collections.Counter(nums)
        return [a for a in count if count[a-1] == count[a+1] == count[a] - 1 == 0]