# https://leetcode.com/problems/peeking-iterator/

# Below is the interface for Iterator, which is already defined for you.
from collections import deque

class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator(object):
    
    # Runtime: 12 ms, faster than 98.25% of Python online submissions for Peeking Iterator.
    # Memory Usage: 13.6 MB, less than 70.18% of Python online submissions for Peeking Iterator.
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self.q = deque()
        while iterator.hasNext():
            self.q.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        
        return self.q[0]
        

    def next(self):
        """
        :rtype: int
        """
        val = self.q.popleft()
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)>0
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].