# https://leetcode.com/problems/count-sorted-vowel-strings/
class Solution:
    
    # HEHE
    def countVowelStrings(self, n: int) -> int:
        
        result = [        
        5,
        15,
        35,
        70,
        126,
        210,
        330,
        495,
        715,
        1001,
        1365,
        1820,
        2380,
        3060,
        3876,
        4845,
        5985,
        7315,
        8855,
        10626,
        12650,
        14950,
        17550,
        20475,
        23751,
        27405,
        31465,
        35960,
        40920,
        46376,
        52360,
        58905,
        66045,
        73815,
        82251,
        91390,
        101270,
        111930,
        123410,
        135751,
        148995,
        163185,
        178365,
        194580,
        211876,
        230300,
        249900,
        270725,
        292825,
        316251
        ]
        
        return result[n-1]
    
    
    # Generating above sequence using formula n = n*(n-1)*(n-2)*(n-3) //24
    def countVowelStrings(self, n: int) -> int:
        
        return [(i*(i-1)*(i-2)*(i-3))//24 for i in range (5, 56)][n-1]
    
    
    # Recursion / Brute Force
    def countVowelStrings(self, n: int) -> int:
        
        array = ["a","e","i","o","u"]
        self.result =[]
        def helper(n, s, index):
            
            if n==0:
                self.result.append(s)
                return 
            
            for i in range(index, len(array)):
                helper(n-1, s+array[i], i)
                
            return self.result
        
        return len(helper(n, "", 0))
    
    
    # Expected Solution
    
    # Runtime: 33 ms, faster than 80.43% of Python3 online submissions for Count Sorted Vowel Strings.
    # Memory Usage: 13.9 MB, less than 27.45% of Python3 online submissions for Count Sorted Vowel Strings.
    
    def countVowelStrings(self, n: int) -> int:
        
        array = [1,1,1,1,1]
        
        for i in range (n):
            for j in range(3, -1, -1):
                array[j]+=array[j+1]
        
        return sum(array)
            