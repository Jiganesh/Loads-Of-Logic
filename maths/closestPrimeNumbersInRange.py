
import math
from typing import List

class Solution:
            
    
    # Interview Acceptable
    def closestPrimes(self, left: int, right: int) -> List[int]:


        is_composite = [False] * (right+1)
        last_prime = -1
        result = [-1, -1]

        for prime_number in range (2, right+1):
            if not is_composite[prime_number]:
                for number in range(prime_number*2, right+1, prime_number):
                    is_composite[number]=True

                if left<= prime_number <= right:
                    if last_prime == -1:  # Condition there as we need last_prime in next conditions
                        last_prime = prime_number
                    
                    elif result == [-1, -1]:
                        result = [last_prime, prime_number]
                    
                    elif prime_number-last_prime < result[1]-result[0] :
                        result = [last_prime, prime_number]
                        if prime_number - last_prime <=2:
                            return result

                    last_prime = prime_number

        return result
                        
            
    
    # Interview Acceptable
    def closestPrimes(self, left: int, right: int) -> list[int]:

        
        def is_prime(number):
            
            for num in range(2, int(math.sqrt(number))+1):
                if number%num==0:
                    return False

            return True

        last_prime = -1
        result = [-1, -1]

        for prime_number in range (2, right+1):
            if is_prime(prime_number):


                if left<= prime_number <= right:
                    if last_prime == -1:  # Condition there as we need last_prime in next conditions
                        last_prime = prime_number
                    
                    elif result == [-1, -1]:
                        result = [last_prime, prime_number]
                    
                    elif prime_number-last_prime < result[1]-result[0] :
                        result = [last_prime, prime_number]

                    last_prime = prime_number

        return result
    
    def closestPrimes(self, left: int, right: int) -> list[int]:
        
        def is_prime(number):    
            for num in range(2, int(math.sqrt(number))+1):
                if number%num==0:
                    return False
            return True
        
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)
        
        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])


                        
            
