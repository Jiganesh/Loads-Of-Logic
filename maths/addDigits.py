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

    # TC : O(1)
    # SC : O(1)
    def addDigits(self, num: int) -> int:

        if num == 0 :
            return 0
        elif num %  9 == 0:
            return 9
        else :
            return num % 9

         
        
print(Solution().addDigits(38))