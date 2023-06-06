# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):

        self.stack = []
        self.index = 0
        

    def next(self, price: int) -> int:

        self.index +=1

        while self.stack and self.stack[-1][-1] <= price:
            self.stack.pop()

        if self.stack:
            ans = self.index - self.stack[-1][0]
        else:
            ans = self.index
        self.stack.append((self.index, price))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)