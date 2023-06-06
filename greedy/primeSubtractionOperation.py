# https://leetcode.com/problems/prime-subtraction-operation/

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        
        primes = [True]*(1000)
        primes[0] = primes[1] = False
        
        for num in range (2, 1000):
            if primes[num]==True:
                for mul in range (num*2, 1000, num):
                    primes[mul]=False
                    
        prime_nums = [i for  i in range (0, 1000) if primes[i]==True]
        

        for ind in range (len(nums)-2, -1, -1):
            last_number = nums [ind+1]
            curr_number = nums [ind]

            if curr_number >= last_number:
                for prime_number in prime_nums:
                    if prime_number >= curr_number:
                        break
                    
                    if curr_number - prime_number < last_number:
                        nums[ind] = curr_number - prime_number
                        break

        print(nums)
        for ind in range (1, len(nums)):
            if nums[ind-1] >= nums[ind]:
                return False
        return True