# https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        result = 0
        current_capacity = capacity

        for ind, plant in enumerate(plants):
            if current_capacity >= plant:
                current_capacity -= plant
                result+=1
            else:
                current_capacity = capacity
                current_capacity-= plant
                result += ind
                result += ind+1
            
        return result


    # Modified above code
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        result = 0
        current_capacity = capacity

        for ind, plant in enumerate(plants):
            if current_capacity < plant:
                current_capacity = capacity
                result += 2 * ind

            result += 1 
            current_capacity -= plant
            
        return result