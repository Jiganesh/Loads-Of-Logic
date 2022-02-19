# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums):
        
        #1 with string and len
        count=0
        for i in range(0,len(nums)):
            if (len(str(nums[i]))%2==0): count+=1
        return count
    
        '''
        #2 Using division
        count=0
        for i in nums:
            cur=0
            while(i>0):
                cur+=1
                i=i//10
            if cur%2==0: count+=1
        return count       
       
        #3 using log and floor 
        #floor(log10(num)) gives 1 value less than length of integer ie odd
        return sum((floor(log10(i)))%2 for i in nums)
        '''
