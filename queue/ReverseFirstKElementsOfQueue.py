# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0


from queue import Queue


def reverseElements(q, k):
    # Using a stack
    n = q.qsize()
    stack, q2 = [], []
    for items in range(k):
        stack.append(q.get())
    for op in range(k):
        q.put(stack.pop())
    for topop in range(n-k):
        q.put(q.get())
    return q


'''

#Only Using Queue
def reverse_que(que):
    if que.empty():
        return
    item = que.get()
    reverse_que(que)
    que.put(item)


def reverseElements(q, k):
    n = q.qsize()
    q1, q2 = Queue(), Queue()
    for items in range(n):
        if items < k:
            q1.put(q.get())
        else:
            q2.put(q.get())
        
    reverse_que(q1)

    for op in range(n):
        if op < k:
            q.put(q1.get())
        else:
            q.put(q2.get())
       
    return q

'''

# for checking


def print_que(que):
    while que.qsize() != 0:
        print(que.get(), end=" ")
    print()


# in question q was, taken input from Queue module hence get and put are used for it.
k = 3
que = Queue()
que.put(1)
que.put(2)
que.put(3)
que.put(4)
que.put(5)

print_que(reverseElements(que, k))
