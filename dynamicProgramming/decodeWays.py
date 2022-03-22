# https://leetcode.com/problems/decode-ways/

# Solution : https://leetcode.com/problems/decode-ways/discuss/621312/Python-DP-and-Recursion-w-Explanation

class Solution(object):

    # Submitted by Jiganesh


    # TC : O(N)
    # SC : O(N)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = { "" : 1 }
        def helper(s):

            if  s in dp  :
                return dp[s]

            first, second = 0,0

            if 1<=int(s[0])<=9:
                first = helper(s[1:])

            if len(s)>=2 and( s[0]=="1" or( s[0]=="2" and  0<=int(s[1])<=6)):
                second = helper(s[2:])

            dp[s]= first +second

            return first+second

        return helper(s)