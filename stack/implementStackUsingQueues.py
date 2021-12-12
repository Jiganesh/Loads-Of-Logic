#https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    
        #lists use O(n) for append, pop so less efficient
#     def __init__(self):
#         self.q1=[]
#         self.q2=[]

#     def push(self, x: int) -> None:
#         self.q1.append(x)
#         self.q2=self.q1[::-1]

#     def pop(self) -> int:
#         p=self.q2.pop(0) #first in first out
#         self.q1=self.q2[::-1]
#         return p

#     def top(self) -> int:
#         return self.q2[0]

#     def empty(self) -> bool:
#         return len(self.q1)==0

#----------------------------------------------------

    # Runtime: 24 ms, faster than 94.55% of Python3 online submissions for Implement Stack using Queues.
    # Memory Usage: 14.4 MB, less than 43.44% of Python3 online submissions for Implement Stack using Queues.

    #With TWO QUEUES

#     from collections import deque
#     def __init__(self):
#         self.queue1=deque()
#         self.queue2=deque()

#     def push(self, x: int) -> None:
#         self.queue1.append(x)
#         self.queue2.append(x)
#         self.queue2.reverse()
        
#     def pop(self) -> int:
#         if self.queue2:
#             popped= self.queue2.popleft()
#             self.queue1= self.queue2
#             self.queue1.reverse()
#             return popped
#         return -1
    
#     def top(self) -> int:
#         return self.queue2[0]

#     def empty(self) -> bool:
#         return len(self.queue1)==0

#Runtime: 20 ms, faster than 98.90% of Python3 online submissions for Implement Stack using Queues.
#Memory Usage: 14.4 MB, less than 43.44% of Python3 online submissions for Implement Stack using Queues.

#With only one Queue
    from collections import deque
    def __init__(self):
        self.queue1=deque()

    def push(self, x: int) -> None:
        siz=len(self.queue1)
        self.queue1.append(x)
        for i in range(siz):
            val=self.queue1.popleft()
            self.queue1.append(val)
        
        
    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        return -1
    
    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()