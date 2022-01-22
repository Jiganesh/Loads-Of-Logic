# https://leetcode.com/problems/gas-station/
# Solution : https://www.youtube.com/watch?v=3wUa7Lf1Xjk

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        array = []
        for i in range (len(gas)):
            array.append(gas[i]-cost[i])
        
        if sum(array)<0:
            return -1;
        
        petrolLeft=-1
        for i in range(len(array)):
            if petrolLeft==-1: 
                position =i
                
            if petrolLeft+array[i]>=0:
                petrolLeft+=array[i]
            else :
                petrolLeft=-1
                
        return position