# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(string):
            result = ""
            for num in string:
                result += "1" if num == "0" else "0"

            return result


        def helper(n):

            if n==1:
                return "0"
            
            prev_s = helper(n-1)
            return prev_s + "1" + invert(prev_s)[::-1]

        return helper(n)[k-1]

