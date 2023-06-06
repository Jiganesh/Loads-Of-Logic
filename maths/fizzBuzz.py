# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []
        def helper(num):
            if num%15==0:
                return "FizzBuzz"
            if num%5==0:
                return "Buzz"
            if num%3==0:
                return "Fizz"
            return str(num)

        for i in range(1, n+1):
            answer.append(helper(i))

        return answer