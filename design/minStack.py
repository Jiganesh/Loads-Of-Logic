# https://leetcode.com/problems/min-stack/

class MinStack:
    
    # Runtime: 62 ms, faster than 87.61% of Python3 online submissions for Min Stack.
    # Memory Usage: 18.1 MB, less than 50.26% of Python3 online submissions for Min Stack.

    def __init__(self):
        
        self.stack = []
        self.minstack =[]
        

    def push(self, val: int) -> None:
        
        if self.stack :
            self.stack.append(val)
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.stack.append(val)
            self.minstack.append(val)
        

    def pop(self) -> None:
        
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minstack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()