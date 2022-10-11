# Problem Link: https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper():
            return True
        else:
            for i in range(len(word)):
                if i==0 and word[i].isupper()==False:
                    return False
                elif i!=0 and word[i].islower()==False:
                    return False
        return True
    
    # We will apply the Brute force algorithm for this problem
    # We shall traverse the entire string to make sure the conditions follow