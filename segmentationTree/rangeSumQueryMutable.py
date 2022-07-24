from re import I


class SegmentationNode:
    
    def __init__(self,start, end, value):
        
        self.start = start
        self.end = end
        self.value = value
        self.left = None   
        self.right = None
        
class SegmentationTree:
    
    def __init__(self, nums):
        
        self.root = self.build( 0, len(nums)-1, nums)
    
    def build (self, start, end, nums) :
        
        if start > end :
            return None
        
        if start == end :
            return SegmentationNode(start, end, nums[start])
        
        else :
            mid = start + (end-start)//2
            node = SegmentationNode(start, end, 0)
            node.left = self.build(start, mid, nums)
            node.right = self.build(mid+1, end, nums)
            node.value = node.left.value + node.right.value
            return node
        
    def update (self, node , position, value):
        if not node : return 0
        
        if node.start> position and position< node.end:
            return 0
        
        if node.start == position and node.end == position:
            node.value = value
            return value
        else:
            midpoint= (node.start +node.end)//2
            if position<= midpoint:
                self.update(node.left, position, value)
            else:
                self.update(node.right, position, value)

            
        left = node.left.value if node.left else 0
        right = node.right.value if node.right else 0
        
        node.value = left + right
        return  node.value
    
    
    

st = SegmentationTree([1,3,4,5])                
print(st.root.value)
st.update(st.root, 1, 4)
print(st.root.value)

print(st.root.value)
            
    