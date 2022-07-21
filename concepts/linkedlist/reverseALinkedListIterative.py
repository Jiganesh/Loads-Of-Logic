from requests import head


class Node :
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList :
    def __init__(self) -> None:
        self.head=None
        
    def add (self,val):
        
        node =Node(val)
        if not self.head:
            self.head=node
            
        else:
            current =self.head
            while current.next:
                current=current.next
            current.next = node
            
        return head
    
    def reverse (self):
        
        current = self.head
        previous = None
        
        while current:
            temp = current.next
            current.next=previous
            previous =current
            current = temp
            
        self.head=previous
        self.printll()
    
    def printll(self):
        current = self.head
        while current:
            print(current.val, end="----->")
            current=current.next
        print()
            

ll = LinkedList()
ll.add(5)
ll.add(6)
ll.add(8)
ll.add(9)
ll.printll()
ll.reverse()