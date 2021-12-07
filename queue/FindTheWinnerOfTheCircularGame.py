#https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        #Solution with list
        
        que=[]
        for friend in range(n):
            que.append(friend+1)
        #print(que)
        while len(que)>1:
            for i in range(k-1):
                que.append(que.pop(0))
                #print(que)
            que.pop(0)
            #print(que)
            
        return que[0]
        '''
        
        '''
        #Using deque 
        
        from collections import deque
        que=deque([])
        for friends in range(n):
            que.append(friends+1)
        #print(que)
        while len(que)>1:
            for i in range(k-1):
                que.append(que.popleft())
                #print(que)
            que.popleft()
            #print(que)
            
        return que[0]
            
        '''
        '''
        #Using head pointer
        
        from collections import deque
        que=deque([])
        for friends in range(n):
            que.append(friends+1)
        #print(que)
        
        head=0
        while len(que)!=1:
            if head!=k-1:
                que.append(que.popleft())
                head+=1
            else:
                que.popleft()
                head=0
            #print(que, head)
        
        return que[0]
        
        '''
        '''
        #Improving Head pointer method (Better solution)
        
        from collections import deque
        que=[i+1 for i in range(n)]
        
        head=0
        while len(que)>1:
            head=(head+k-1)%len(que)
            que.pop(head)
        
        return que[0]
        '''
        #Using rotating deque (Best solution for python amoung these)
        #rotate deque with negative value means rotating 0 to k ie from front
        
        import collections
        que=collections.deque([i for i in range(1, n + 1)])
            
        while len(que)>1:
            que.rotate(-k)
            que.pop()
            #print(que)
        
        return que[0]
            