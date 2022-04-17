# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/x


from collections import Counter

class Solution:
    
    # Runtime: 974 ms, faster than 75.00% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
    # Memory Usage: 28.4 MB, less than 25.00% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
    
    def minimumRounds(self, tasks) -> int:
        
        dictionary = Counter(tasks)
        ans =0
        
        for i in dictionary :
            
            if dictionary[i]==1:
                return -1
            
            ans +=dictionary[i]//3
            
            if (dictionary[i]%3):
                ans+=1
        
        return ans
        
        