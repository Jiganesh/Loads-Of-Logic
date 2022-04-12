# https://leetcode.com/problems/find-players-with-zero-or-one-losses/


from collections import Counter

class Solution:
    
    # Runtime: 2539 ms, faster than 63.65% of Python3 online submissions for Find Players With Zero or One Losses.
    # Memory Usage: 69.3 MB, less than 30.02% of Python3 online submissions for Find Players With Zero or One Losses.

    def findWinners(self, matches):
        
        dictionary = {}
        
        for i in matches:
            winner = i[0]
            loser = i[1]
            
            if winner in dictionary :
                dictionary[winner][0]+=1
            else :
                dictionary[winner]= [1, 0]
            if loser in dictionary:
                dictionary[loser][1]+=1
            else:
                dictionary[loser]=[0,1]
                
        wonall = []
        lostone =[]
        
        for key , values in dictionary.items():
            
            if values[1]==0:
                wonall.append(key)
            
            if values[1]==1:
                lostone.append(key)
                
        wonall.sort()
        lostone.sort()
        
        return [wonall, lostone]
    
    # Neat Code
    def findWinners(self, matches):
        
        winnersOfMatches = [i[0] for i in matches]
        loserOfMatches = [i[1] for i in matches]
        
        allWin = list(set(winnersOfMatches)- set(loserOfMatches))
        
        dictionaryOfLosers = Counter(loserOfMatches)
        oneLost = [ i for i in dictionaryOfLosers if dictionaryOfLosers[i]==1]
        
        return[sorted(allWin), sorted(oneLost)]
                
                
            