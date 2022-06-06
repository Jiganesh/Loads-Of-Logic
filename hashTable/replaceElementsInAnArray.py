# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    # Runtime: 1556 ms, faster than 40.00% of Python3 online submissions for Replace Elements in an Array.
    # Memory Usage: 70.3 MB, less than 40.00% of Python3 online submissions for Replace Elements in an Array.
    def arrayChange(self, nums, operations) :
        
        element_index_dictionary =  {nums[i]:i for i in range (len(nums))}
        
        for i, j in operations:
            index = element_index_dictionary[i]
            del element_index_dictionary[i]
            element_index_dictionary[j]=index
        
        result = [0]*len(element_index_dictionary)
        
        for key , value in element_index_dictionary.items():
            result[value] = key
        return result