# https://leetcode.com/problems/four-divisors/

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int: 

        memoize = defaultdict(int) 

        def has_four_divisors(num):

            if memoize[num]: 
                print(num, memoize[num])
                return memoize[num]

            divisors = set()

            for i in range(1, int(num**(0.5))+1):
                if num%i==0:
                    divisors.add(i)
                    divisors.add(num//i)
                if len(divisors) > 4: return 0

            if len(divisors) == 4 : 
                memoize[num] = sum(divisors)
            return memoize[num]
                
        return sum(map(has_four_divisors, nums))
            

