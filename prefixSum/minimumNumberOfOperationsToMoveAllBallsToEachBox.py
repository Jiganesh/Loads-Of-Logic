# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)

        left = [0] * (n)
        count_of_ball = int(boxes[0])


        for i in range(1,n):
            left[i] = left[i-1] + count_of_ball
            count_of_ball += int(boxes[i])

        print(left)


        right = [0] * (n)
        count_of_ball = int(boxes[-1])

        for i in range(n-2, -1, -1):
            right[i] = right[i+1]+ count_of_ball
            count_of_ball += int(boxes[i])
        
        result = [0]*n
        for i in range(n):
            result[i]= left[i]+right[i]

        return result

