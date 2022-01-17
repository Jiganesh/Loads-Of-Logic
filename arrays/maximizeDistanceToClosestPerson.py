# https://leetcode.com/problems/maximize-distance-to-closest-person/
# Solution : https://www.youtube.com/watch?v=Ngf1XUDfK7M

class Solution:
    
    # TC : O(N)
    # SC : O(N)
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        n = len(seats)
        left = [n]*n
        right = [n]*n
        
        
        for i in range(n):
            if seats[i]==1:
                left[i]=0
            elif i>0 :
                left[i]=left[i-1]+1
              
        
        for i in range(n-1, -1,-1):
            if seats[i]==1:
                right[i]=0
            elif i<n-1:
                right[i]=right[i+1]+1
    
        
        maximumDistance =float('-inf')
        for i in range(n):
            minimumDistanceBetweenRightAndLeftOne = min(left[i],right[i])
            maximumDistance = max(minimumDistanceBetweenRightAndLeftOne, maximumDistance)
            
        return maximumDistance
    
    
    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 108 ms, faster than 84.75% of Python online submissions for Maximize Distance to Closest Person.
    # Memory Usage: 14.6 MB, less than 33.90% of Python online submissions for Maximize Distance to Closest Person.
    
    def maxDistToClosestApproach2(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seatsAvailable = len(seats)
        firstOccupiedSeat = -1
        countOfZeroBetweenTwoSeats = 0
        maximumDistance = float('-inf')
        
        for i in range(seatsAvailable):
            
            if seats[i]==0:
                countOfZeroBetweenTwoSeats+=1
            else:
                if firstOccupiedSeat == -1 :
                    maximumDistance = countOfZeroBetweenTwoSeats
                    firstOccupiedSeat =i
                else :
                    maximumDistance = max(maximumDistance,(countOfZeroBetweenTwoSeats+1)//2)
                countOfZeroBetweenTwoSeats=0
                    
        return max(maximumDistance, countOfZeroBetweenTwoSeats)
    
        '''
        Example : 
        
        1 0 0 0 0 1 0
        
        We record the first occurence of one and count the zeros till next occurence 
        We find the middle position in between next occurence and note maximum in it
        
        edge cases : 
        
        0,0,0,0,1
        Till we find our first occurence of one we substitue the count in maximum distance
        Makes sense right
        
        1,0,0,0,0,0
        At last we check the maximum value so that we can get rightmost seat
        
        '''