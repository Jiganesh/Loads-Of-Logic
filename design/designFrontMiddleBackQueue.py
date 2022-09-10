# https://leetcode.com/problems/design-front-middle-back-queue/

# Cheating Method LOL O(N)

class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.q)//2
        self.q.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        return self.q.pop(0) if self.q else -1

    def popMiddle(self) -> int:
        mid = (len(self.q)-1)//2
        return self.q.pop(mid) if self.q else -1
    
    def popBack(self) -> int:
        return self.q.pop() if self.q else -1


from collections import deque

# TC: O(1)
# SC : O(N)

# Runtime: 77 ms, faster than 91.45% of Python3 online submissions for Design Front Middle Back Queue.
# Memory Usage: 14.7 MB, less than 14.13% of Python3 online submissions for Design Front Middle Back Queue.

class FrontMiddleBackQueue:

    def __init__(self):
        
        self.A  = deque([])
        self.B  = deque([])

    def pushFront(self, val: int) -> None:
        self.A.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:

        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)
        self.balance
        
    def pushBack(self, val: int) -> None:
        self.B.append(val)
        self.balance()
        
    def popFront(self) -> int:
        val = self.A.popleft( ) if self.A else -1
        self.balance()
        return val

    def popMiddle(self) -> int:
        val = self.A.pop() if self.A else -1
        self.balance()
        return val

    def popBack(self) -> int:
        val = (self.B or self.A or[-1]).pop()
        self.balance()
        return val
        
    def balance (self):
        if len(self.A)  > len(self.B)+1:
            self.B.appendleft(self.A.pop())
        
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
        
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()