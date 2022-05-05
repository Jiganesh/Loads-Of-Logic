from collections import *
# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    
    # Runtime: 44 ms, faster than 41.12% of Python3 online submissions for Implement Stack using Queues.
    # Memory Usage: 13.9 MB, less than 76.44% of Python3 online submissions for Implement Stack using Queues.

    def __init__(self):
        self.q = deque ()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()