class heap:
    
    def __init__(self) -> None:
        self.array = []
        
        
    def heapify(self, n, i):
                
        largest = i 
        left = 2*i+1
        right = 2*i+2

        if left < n and self.array[largest]< self.array[left]:
            largest = left
        if right < n and self.array[largest]< self.array[right]:
            largest = right
        if largest != i:
            self.array[largest],self.array[i] = self.array[i], self.array[largest]
            self.heapify(n, largest)
            
    def push (self,  number):
        n = len(self.array)
        if n == 0:
            self.array.append(number)
        else:
            self.array.append(number)
            for i in range ((n//2)-1, -1, -1):
                self.heapify(n, i)
                

        
    def pop(self):
        temp = self.array
        if len(self.array) == 0:
            return None
        else:
            n = len(self.array)
            for i in range (n//2 , -1, -1):
                self.heapify(n, i)
            max = self.array [0]
            self.array = self.array[1:]
            return max
            
                
                
    def heap_sort(self):
        
        temp = self.array
        n = len(self.array)
        for i in range(n//2-1,-1,-1):
            self.heapify(n, i)
        
        for i in range (n-1, -1, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i,0)
                
        print(self.array)
        self.array = temp
h = heap()
h.push(5)
h.push(6)
h.push(2)
h.push(4)
h.push(3)
h.heap_sort()
h.push(55)
h.push(52)
h.pop()
h.heap_sort()
