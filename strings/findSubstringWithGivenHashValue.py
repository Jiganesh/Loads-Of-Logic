# https://leetcode.com/problems/find-substring-with-given-hash-value/
# Concept : https://www.youtube.com/watch?v=BfUejqd07yo
# Solution : https://www.youtube.com/watch?v=P7dX86HdNqc&t=895s
# Solution : https://www.youtube.com/watch?v=bmX2_mal8YQ&t=611s

class Solution(object):
    
    # Submittted  by @Jiganesh
    
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        
        s = s[::-1]

        firstSubstringValue = ord(s[0])%96

        for i in range(1,k):
            firstSubstringValue = (firstSubstringValue*power+ ord(s[i])-96)
        res = s[0:0+k][:-1]


        for i in range( len(s)-k):
            
            firstSubstringValue = ((firstSubstringValue- (ord(s[i])%96)*pow(power,k-1))*power + ord(s[i+k])%96)%modulo

            if firstSubstringValue == hashValue:
                res = s[i+k:i:-1]
        return res

    # From : https://leetcode.com/problems/find-substring-with-given-hash-value/discuss/1730321/JavaC%2B%2BPython-Sliding-Window-%2B-Rolling-Hash
    # TC : O(N)
    # SC : O(1)
    
    # Well Written Solution
    def subStrHash(self, s, p, m, k, hashValue):
        def val(c):
            return ord(c) - ord('a') + 1
            
        res = n = len(s)
        pk = pow(p,k,m)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * p + val(s[i])) % m
            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % m
            if cur == hashValue:
                res = i
        return s[res: res + k]


n= 3
while n:
    s = input()
    power = int(input())
    modulo = int(input())
    k = int(input())
    hashValue = int(input())
    print(Solution().subStrHash(s, power, modulo, k, hashValue))
    n-=1
    
    
'''
TestCases :

"leetcode"
7
20
2
0
"fbxzaad"
31
100
3
32
"xmmhdakfursinye"
96
45
15
21
'''   

