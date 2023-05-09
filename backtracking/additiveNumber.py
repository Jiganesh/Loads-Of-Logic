# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        N = len(num)

        def helper(first, second):

            sequence = [str(first), str(second)]
            total_length = sum(len(x) for x in sequence)


            while total_length < N:
                third = str(int(sequence[-1]) + int(sequence[-2]))
                total_length += len(third)
                sequence.append(third)
            return "".join(sequence)
                

        for left in range (1, N):
            for right in range (left+1, N):

                first_number = num[:left]
                second_number = num[left: right]

                generated_num = helper(int(first_number), int(second_number))
                if generated_num == num:
                    return True

        return False


# Testcases
# 1023, 101, 0235813

