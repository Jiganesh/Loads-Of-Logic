# https://leetcode.com/problems/coin-change/

class Solution(object):
    
    # Brute Force Approach
    # TLE
    
    # TC: O(2^m)
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array=[]
        count=0
        result = self.helper(coins, amount, count, array)
        a= float('inf')
        for i in result:
            a= min(a, i)
        return a if a!= float('inf') else -1
    
    
    
    def helper(self, coins, amount, count=0, array=[]):
        
        if amount == 0:
            array.append(count)
    
        if amount >0:
            for i in coins:
                count+=1
                self.helper(coins, amount-i, count, array)
                count-=1
        return array
    
    
    # TC:O(N*M) N is number of Coins and M is amount
    # SC:O(M) where M is amount
    
    # Instead of float('inf') we can also use amount+1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount ==0 : return 0
        
        amountArr = [float('inf') for i in range(amount+1)]
        amountArr [0]=0
        
        for coin in coins:
            for currentamount in range(amount+1):
                if coin <= currentamount:
                    amountArr[currentamount] = min(amountArr[currentamount], 1+amountArr[currentamount-coin])
        
        return amountArr[currentamount] if amountArr[currentamount] != float('inf') else -1       
        
        
        
        
print(Solution().coinChange([1,2,5],11)) #3
print(Solution().coinChange([2],1)) #-1
print(Solution().coinChange([2],3)) #-1
print(Solution().coinChange([4,5,7],3)) #-1
print(Solution().coinChange([4,5,7],11)) #
print(Solution().coinChange([1],0)) #0
print(Solution().coinChange([2],4)) #2
print(Solution().coinChange([186,419,83,408],6249)) #20
                
                