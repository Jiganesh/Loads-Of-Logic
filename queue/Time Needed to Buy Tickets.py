#https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        '''
        #brute force:
        count=0
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    count+=1
                if tickets[k]==0:
                    break
        return count
        '''
        '''
        #without for loop
        count=0
        i=0
        n=len(tickets)
        while tickets[k]:
            if tickets[i]>0:
                tickets[i]-=1
                count+=1
            if i==n-1:
                i=0
            else:
                i+=1
        return count
        '''
        #O(n) solution
        count=0
        for i,j in enumerate(tickets):
            # for all positions before k it will buy all tickets or get till kth place
            if i<=k:
                count+=min(j,tickets[k])
            else:
                # for all positions after k it will buy all tickets or get 1 less than kth place
                count+=min(j,tickets[k]-1)
            
        return count