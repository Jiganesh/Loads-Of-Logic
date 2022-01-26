# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    
    # Submitted by @Jiganesh
    
    # TC : O(NLogN) where N = m+n
    # TC : O(N) where N = m+n
        
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        sortedList1  = self.helper(root1,[])
        sortedList2  = self.helper(root2,[])
        listed = []
        if sortedList1:
            listed +=sortedList1
        if sortedList2:
            listed+= sortedList2
            
            
        listed =[]
        pointer1 = 0;
        pointer2 = 0;
        
        while pointer1< len(sortedList1) or pointer2< len(sortedList2):
            if sortedList1[pointer1]<sortedList2[pointer2]:
                listed.append(sortedList1[pointer1])
                pointer1+=1
            else:
                listed.append(sortedList2[pointer2])
                pointer2+=1
        
        return sorted(listed)
            
        
    def helper( self, root, array=[]):
        
        if root == None:
            return 
        else:
            self.helper(root.left,array);
            array.append(root.val);
            self.helper(root.right,array);
            
        return array;
    
    # Submitted by @Jiganesh
    # Optimized
    
    # TC : O(N) where N = m+n
    # SC : O(N) where N = m+n
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        
        sortedList1, sortedList2 =[],[]
        self.helper(root1,sortedList1)
        self.helper(root2,sortedList2)

        listed =[]
        pointer1 = 0;
        pointer2 = 0;
        
        while pointer1< len(sortedList1) and pointer2< len(sortedList2):
            if sortedList1[pointer1]<sortedList2[pointer2]:
                listed.append(sortedList1[pointer1])
                pointer1+=1
            else:
                listed.append(sortedList2[pointer2])
                pointer2+=1
                
        return listed +sortedList1[pointer1:]+ sortedList2[pointer2:]
        
        
        
    def helper( self, root, array=[]):
        
        if root == None:
            return 
        else:
            self.helper(root.left,array);
            array.append(root.val);
            self.helper(root.right,array);
            
        return array;
    
# TestCases : Test in Leetcode
"""
[]
[5,1,7,0,2]
[2,1,4]
[1,0,3]
[1,null, 8]
[8,1]

"""
            