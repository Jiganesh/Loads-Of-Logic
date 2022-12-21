# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
# Refer cool Seive Technique used = https://www.youtube.com/watch?v=0DT1_B0PVak
from math import sqrt


class Solution:
    
    # TC: O(nlogn)
    def smallestValue(self, n: int) -> int:

        seive = [i for i in range(n+1)]
        def computing_seive (n):
            

            limit = int(sqrt(n)+1)
            for i in range(2, limit):
                if seive[i] == i:
                    for j in range(i, n+1, i):
                        if seive[j]==j:
                            seive[j] =  i

        computing_seive(n)
        
        curr_number = n
        result = float("inf")

        while curr_number > 0:
            summation = 0
            number = curr_number

            while curr_number !=1 :
                summation += seive[curr_number]
                curr_number //= seive[curr_number]

            if summation == number : return min(result, summation)
            curr_number = summation

            
            result = min(summation, result)
            if seive[curr_number] == curr_number: return result

        return result