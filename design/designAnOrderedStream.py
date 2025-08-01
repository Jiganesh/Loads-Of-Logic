# https://leetcode.com/problems/design-an-ordered-stream

class OrderedStream:

    # TC : O(N)
    # SC : O(N)

    def __init__(self, n: int):
        self.stream = [None]*(n+1)
        self.pointer = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:

        self.stream[idKey] = value

        if self.pointer == idKey:  # Check if pointer is on key provided

            # Yes - then check how many values are there till we find None
            while self.pointer < len(self.stream) and self.stream[self.pointer]:
                self.pointer+=1

        #with self.pointer we determined endpoint of chunck and kept our pointer on end of chunk
        return self.stream[idKey:self.pointer]

        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)