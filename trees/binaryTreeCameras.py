# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

class Solution:
    # Runtime: 47 ms, faster than 90.16% of Python3 online submissions for Binary Tree Cameras.
    # Memory Usage: 14.6 MB, less than 7.09% of Python3 online submissions for Binary Tree Cameras.
    def minCameraCover(self, root) -> int:
        
        self.camera_count = 0
        
        no_camera = 0
        needs_camera = 1
        has_camera = 2
        covered = 3
        
        def getCameraStatus(root):

            if not root:
                return no_camera
            
            if not root.left and not root.right :
                return needs_camera
            
            left  = getCameraStatus(root.left)
            right = getCameraStatus(root.right)
            
            if left == needs_camera or right ==needs_camera:
                root.val = "*"
                self.camera_count +=1
                return has_camera
            
        
            if left == has_camera or right == has_camera:
                return covered
            
            return needs_camera
        
        

        val = getCameraStatus(root)
        self.camera_count = self.camera_count+1 if val==needs_camera else self.camera_count
        
        q = [root]
        while q:
            print(*[i.val for i in q])
            q = [child for p in q for child in [p.left, p.right] if child]
            
            
        return self.camera_count
            
            
        