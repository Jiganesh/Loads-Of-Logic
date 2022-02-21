# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution(object):
    
    
    # Submitted by Jiganesh
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # Runtime: 78 ms, faster than 100.00% of Python online submissions for Count Integers With Even Digit Sum.
        # Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Count Integers With Even Digit Sum.
        
        count = 0 
        for i in range (1, num+1):
            if sum(int(i) for i in str(i))%2== 0:
                count+=1
        #return count
        
        # Pythonic Version
        #return len([ i for i in range(1, num+1) if sum(int(i) for i in str(i))%2==0])
        
        # Math Logic Version
        
        # Runtime: 23 ms, faster than 100.00% of Python online submissions for Count Integers With Even Digit Sum.
        # Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Count Integers With Even Digit Sum.
        
        # TC : O(n) where n is length of the number
        # SC : O(1)
        summation =0
        temp=num
        while num:
            summation+=num%10
            num//=10
            
        return temp//2 if summation%2==0 else (temp-1)//2
        
        
print(Solution().countEven(10))
print(Solution().countEven(20))
print(Solution().countEven(30))
        
        
        
        
        
        