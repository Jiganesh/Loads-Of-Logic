# https://leetcode.com/problems/product-of-the-last-k-numbers/

# Runtime: 264 ms, faster than 95.15% of Python3 online submissions for Product of the Last K Numbers.
# Memory Usage: 28.9 MB, less than 93.76% of Python3 online submissions for Product of the Last K Numbers.

#the logic is insta of multiplying each value to get product 
#use prefix products while adding the number
#and if latest number is 0 then due to multiplication all its previous values will be zero, so reset the queue
#to get product divide the latest product with number before index k 

class ProductOfNumbers:

    def __init__(self):
        self.queue=[1]
        
    def add(self, num: int) -> None:
        if num==0:
            self.queue=[1]
        else:
            self.queue.append(self.queue[-1]*num)

    def getProduct(self, k: int) -> int:
        n= len(self.queue)
        if k>=n:
            return 0
        else:
            return int(self.queue[-1] // self.queue[-1-k])
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)