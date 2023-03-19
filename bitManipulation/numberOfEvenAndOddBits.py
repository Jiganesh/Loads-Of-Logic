class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0,0]
        bit_ind = 0
        
        while n:
            if n&1:
                if bit_ind&1:
                    result[1]+=1
                else:
                    result[0]+=1
                    
            n = n >> 1
            bit_ind +=1
        return result
