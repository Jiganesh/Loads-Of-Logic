# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num > 9:
            temp = 0
            while num>0:
                temp+=num%10
                num = num//10
            num = temp
        return num
        
print(Solution().addDigits(38))