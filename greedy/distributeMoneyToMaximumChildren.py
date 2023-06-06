# https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        
        if money < children:
            return -1

        money -= children # greedy giving one dollar to each child

        # case where all children get 8 dollars and no remainder
        if money // 7 == children and money % 7 ==0 : 
            return children

        # case where children get 8 dollars except 1 and that child gets 4
        # two children wont be able to get 8 dollars
        if money // 7 == children-1 and money % 7 == 3:
            return children-2

        # case where the last kid doesnt have 8 dollars or number of kid not able to get 8 dollar
        # example for later case is money = 2 and children = 2
        return min(children-1, money//7)