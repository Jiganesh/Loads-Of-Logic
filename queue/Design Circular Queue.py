#https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    '''
    #without using head tail pointers
    def __init__(self, k: int):
        self.que=[None]*k
    
    def enQueue(self, value: int) -> bool:
        if None in self.que:
            self.que[self.que.index(None)]=value
            return True
        return False

    def deQueue(self) -> bool:
        if self.que[0] is not None:
            self.que.pop(0)
            self.que.append(None)
            return True
        return False
        

    def Front(self) -> int:
        print(self.que)
        if self.que[0] is not None:
            return self.que[0]
        return -1

    def Rear(self) -> int:
        for item in self.que[::-1]:
            if item is not None:
                return item
        return -1

    def isEmpty(self) -> bool:
        print(self.que)
        if None in self.que and len(set(self.que))==1:
            return True
        return False
            

    def isFull(self) -> bool:
        if None not in self.que:
            return True
        return False
    '''
    
    #Optimized Solution
    #Runtime: 60 ms, faster than 97.81% of Python3 online submissions for Design Circular Queue.
    #Memory Usage: 14.8 MB, less than 61.79% of Python3 online submissions for Design Circular Queue.
    def __init__(self, k: int):
        self.que=[None]*k
        self.front=0
        self.rear=-1
        self.size=0
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear=(self.rear+1)%len(self.que)
            self.que[self.rear]=value
            self.size+=1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front=(self.front+1)%len(self.que)
            self.size-=1
            return True
        

    def Front(self) -> int:
        if self.size!=0:
            return self.que[self.front]
        return -1

    def Rear(self) -> int:
        if self.size!=0:
            return self.que[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.size==0
            

    def isFull(self) -> bool:
        return self.size==len(self.que)

    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
