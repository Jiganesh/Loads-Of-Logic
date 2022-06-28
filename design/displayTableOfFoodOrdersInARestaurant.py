# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import List
from collections import defaultdict 
from itertools import Counter

class Solution:
    
    # Runtime: 604 ms, faster than 61.61% of Python3 online submissions for Display Table of Food Orders in a Restaurant.
    # Memory Usage: 38.7 MB, less than 33.93% of Python3 online submissions for Display Table of Food Orders in a Restaurant.
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        set_food = set()
        table = defaultdict(Counter)
        # defaultdict(lambda:default(int))
        
        for order in orders:
            name, number, food = order
            set_food.add(food)
            table[number][food]+=1
            
        set_food = sorted(list(set_food))  # sort one
        dictionary_header = {set_food[i]: i for i in range(len(set_food))}
            
        
        result = []
        for number in table:
            row =[int(number)]
            for food in dictionary_header:
                row.append(table[number][food])
            result.append(row)
            
        result.sort()  # sort two
        for  i in range (len(result)):
            result[i] =  list(map(str, result[i]))
            
        header = ["Table"]
        header.extend(set_food)
        
        
        return [header] + result
    
    
        