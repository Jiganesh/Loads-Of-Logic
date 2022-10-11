# Problem link: https://leetcode.com/problems/add-to-array-form-of-integer/


from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #         In this problem we have to convert the given list into an integer
        #         Add the number K to the formed integer 
        #         And convert the number into the array
        #         We return the final array
        
        num = list(map(str, num))
        number = "".join(num)
        # print(number)
        number = int(number) + k
        
        result = []
        for i in str(number):
            result.append(i)
        return result

    