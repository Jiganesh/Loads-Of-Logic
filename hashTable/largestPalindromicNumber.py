# https://leetcode.com/problems/largest-palindromic-number/

import heapq
from collections import defaultdict, Counter

class Solution:
    
    # Runtime: 1235 ms, faster than 100.00% of Python3 online submissions for Largest Palindromic Number.
    # Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Largest Palindromic Number.
    
    def largestPalindromic(self, num: str) -> str:
        
        lookup = defaultdict(int)
        for number in num:
            lookup[-(int(number))] +=1
        print(lookup)
        
        heap = list(lookup.keys())
        heapq.heapify(heap)
        
        number_prefix = []
        
        
        while heap:
            key = heapq.heappop(heap)
            value = lookup[key]//2
    
            while value :
                number_prefix.append(-key)
                value-=1
            lookup[key] %= 2
            
        minimum_odd_digit = ""
        minimum = float("inf")
        for key , value in lookup.items():
            if value > 0:
                minimum = min(minimum, key)
        
        if minimum !=float("inf"):
            minimum_odd_digit = str(abs(minimum))
            
        prefix = ""
        suffix = ""
        
        if number_prefix:
            prefix = str(int(''.join(map(str, number_prefix))))
            suffix = "" if int(prefix)==0 else prefix[::-1]
                
        return str(int(prefix + minimum_odd_digit + suffix))
            
    # Optimized Code

    # Runtime: 100 ms, faster than 100.00% of Python3 online submissions for Largest Palindromic Number.
    # Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Largest Palindromic Number.
    
    def largestPalindromic(self, num: str) -> str:
        
        lookup = Counter(num)
        prefix = "".join([ i * (lookup[i]//2) for i in "9876543210"]).lstrip("0")
        mid_digit = max([lookup[num]%2*num for num in lookup])
        suffix = prefix[::-1]
        return prefix+mid_digit+suffix or "0"