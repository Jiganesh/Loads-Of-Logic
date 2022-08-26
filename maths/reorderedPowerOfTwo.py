

class Solution:
    

    # Runtime: 51 ms, faster than 68.45% of Python3 online submissions for Reordered Power of 2.
    # Memory Usage: 13.9 MB, less than 64.17% of Python3 online submissions for Reordered Power of 2.

    def reorderedPowerOf2(self, n: int) -> bool:
        
        def freqdigits (num):
            
            digit_freq = [0]*10
            
            while num:
                digit_freq[num%10]+=1
                num//=10
                
            return digit_freq
        
        
        digit_freq_n = freqdigits(n)
        for power in range (0, 32):
            
            if freqdigits(2**power) == digit_freq_n:
                return True
            
        return False