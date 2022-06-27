# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    
    # Runtime: 96 ms, faster than 68.89% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
    # Memory Usage: 14.7 MB, less than 83.73% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
    
    # TC : O(N)
    # SC : O(1)
    
    def minPartitions(self, n: str) -> int:
        return max(n)
        
        
"""
Logic :

To convert a deci number to binary you will need atlease that many 1's in that position for the deci number of times
Hence you will need atleast max(n) numbers to make the decimal digit

Example 

32 you will need three 1's from atleast three numbers like that 
Its easy bro Just think


"""