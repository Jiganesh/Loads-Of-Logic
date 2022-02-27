#  https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
class Solution(object):
    
    # Submitted by Jiganesh    
    
    # TC : O(S + T)
    # SC : O(sd + td) 
    
    # Runtime: 493 ms, faster than 100.00% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram II.
    # Memory Usage: 18.4 MB, less than 100.00% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram II.
        
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sd, td = {},{}
        
        for i in s:
            if i in sd:
                sd[i]+=1
            else:
                sd[i]=1
        
        for i in t:
            if i in td:
                td[i]+=1
            else:
                td[i]=1
        
        for i in td:
            if i in sd:
                sd[i]= abs(sd[i]-td[i])
            else:
                sd[i]=td[i]
        return(sum(sd.values()))
        
print(Solution().minSteps("night","thing"))
print(Solution().minSteps("leetcode","coats"))
print(Solution().minSteps("adfhsk","dajfslkjfhakjshakhfkjashdfkjadsfakljsdfh"))