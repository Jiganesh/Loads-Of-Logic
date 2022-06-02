# https://leetcode.com/problems/maximum-product-of-word-lengths/
class Solution(object):
    
    # Runtime: 1189 ms, faster than 32.14% of Python online submissions for Maximum Product of Word Lengths.
    # Memory Usage: 15.4 MB, less than 7.14% of Python online submissions for Maximum Product of Word Lengths.
    
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        n=len(words)                        
        char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (char_set[i] & char_set[j]): # if nothing common
                    max_val=max(max_val, len(words[i]) * len(words[j]))
        
        return max_val   
    
    # Runtime: 447 ms, faster than 49.41% of Python online submissions for Maximum Product of Word Lengths.
    # Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Maximum Product of Word Lengths.

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        def get_binary(word):
            binary = 0
            for i in word:
                binary |= 1<< (ord(i)-ord("a")+1)
                
            return binary
            
        n=len(words)                        
        char_bit = [get_binary(i) for i in words]  # precompute binary representation of words
        words = [len(i) for i in words]   # precompute length of words
        max_val = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if (char_bit[i]&char_bit[j] ==0):
                    max_val = max(max_val, words[i]*words[j])
                    
        return max_val   
