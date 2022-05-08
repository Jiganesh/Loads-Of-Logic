# https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    # Runtime: 83 ms, faster than 56.52% of Python3 online submissions for Flatten Nested List Iterator.
    # Memory Usage: 17.8 MB, less than 41.16% of Python3 online submissions for Flatten Nested List Iterator.
    def __init__(self, nestedList):
        
        self.array = []
        def helper(nestedList):
        
            for i in nestedList:
                if i.isInteger():
                    self.array.append(i.getInteger())
                else:
                    helper(i.getList())
                    
        helper(nestedList)
        self.array.reverse()
        

    def next(self) -> int:
        return self.array.pop()
    
    def hasNext(self) -> bool:
        return len(self.array)>0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())