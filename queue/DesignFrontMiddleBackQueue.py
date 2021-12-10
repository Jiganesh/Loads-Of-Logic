# https://leetcode.com/problems/design-front-middle-back-queue/

# Runtime: 60 ms, faster than 99.53% of Python3 online submissions for Design Front Middle Back Queue.
# Memory Usage: 14.9 MB, less than 79.72% of Python3 online submissions for Design Front Middle Back Queue.

from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.que = deque()

    def pushFront(self, val: int) -> None:
        self.que.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        middle=len(self.que)//2
        self.que.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.que.append(val)

    def popFront(self) -> int:
        if len(self.que):
            return self.que.popleft()
        return -1

    def popMiddle(self) -> int:
        n=len(self.que)
        middle=n//2
        if n:
            if (n%2==0):
                self.que.rotate(-(middle-1))
                b=self.que.popleft()
                self.que.rotate(-(n-(middle-1)-1))
            else:
                self.que.rotate(-(middle))
                b=self.que.popleft()
                self.que.rotate(-(n-middle-1))
            return b
        return -1
    
    def popBack(self) -> int:
        if len(self.que):
            return self.que.pop()
        return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()