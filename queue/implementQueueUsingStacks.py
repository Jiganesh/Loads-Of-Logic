#https://leetcode.com/problems/implement-queue-using-stacks/
#Also Known as: Queue from 2 stacks

'''
#1st Approach
class MyQueue: 

    def __init__(self):
        self.firststack=[]
        self.nextstack=[]
        

    def push(self, x: int) -> None:
        self.firststack.append(x)

    def pop(self) -> int:
    #now when we have empty nextstack, we will pop all elements of firststack into nextstack
    #else if nextstack is not empty then pop the last ele from nextstack
    #this was first element in firststack
        if not self.nextstack:
            self.transfer()
                
        return self.nextstack.pop()

    def peek(self) -> int:
        if not self.nextstack:
            self.transfer()
        return self.nextstack[-1]
        

    def empty(self) -> bool:
        return len(self.firststack) + len(self.nextstack) ==0
    
    def transfer(self) ->int:        
        while self.firststack:
            self.nextstack.append(self.firststack.pop())   
'''
#2nd Approach 
class MyQueue:

    def __init__(self):
        self.firststack=[]
        self.nextstack=[]
        

    def push(self, x: int) -> None:
        self.firststack.append(x)
        self.nextstack=(self.firststack[::-1])

    def pop(self) -> int:
        p=self.nextstack.pop()
        self.firststack=(self.nextstack[::-1])
        return p

    def peek(self) -> int:
        return self.nextstack[-1]

    def empty(self) -> bool:
        return len(self.firststack)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
