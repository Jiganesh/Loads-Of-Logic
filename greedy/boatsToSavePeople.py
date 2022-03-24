# https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC : O(NlogN)
    # SC : O(N)
    
    # Runtime: 400 ms, faster than 92.90% of Python online submissions for Boats to Save People.
    # Memory Usage: 18.8 MB, less than 65.81% of Python online submissions for Boats to Save People.
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        
        people.sort()
    
        count = 0
        light, heavy = 0, len(people)-1
        
        while light<=heavy:
            
            if (light==heavy) or people[light]+people[heavy] <= limit :
                count+=1
                light+=1
                heavy-=1
            else :
                count+=1
                heavy-=1
            
        return count
    
    # Aesthetic Solution # Same logic as above
    
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        count = 0
        light, heavy = 0, len(people)-1
        
        while light<=heavy:
            
            if (light==heavy) or people[light]+people[heavy] <= limit :
                light+=1
            count+=1
            heavy-=1
            
        return count