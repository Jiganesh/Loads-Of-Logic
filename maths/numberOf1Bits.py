# https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    
    # Runtime: 46 ms, faster than 5.64% of Python online submissions for Number of 1 Bits.
    # Memory Usage: 13.4 MB, less than 34.23% of Python online submissions for Number of 1 Bits.
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count =0
        
        while n :
            if n&1:count +=1
            n=n>>1
        return count





"""
There are a lot of different ways to solve this problem, starting from transforming number to string and count number of ones. However there is a classical bit manipulation trick you should think about when you have bits problem.

If we have number n, then n&(n-1) will remove the rightmost in binary representation of n. For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000, where & means bitwize operation and. Very convinient, is it not? What we need to do now, just repeat this operation until we have n = 0 and count number of steps.

Complexity It is O(1) for sure, because we need to make no more than 32 operations here, but it is quite vague: all methods will be O(1), why this one is better than others? In fact it has complexity O(m), where m is number of 1-bits in our number. In average it will be 16 bits, so it is more like 16 operations, not 32 here, which gives us 2-times gain. Space complexity is O(1)

class Solution:
    def hammingWeight(self, n):
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans
"""