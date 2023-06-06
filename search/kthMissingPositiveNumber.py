class Solution:

    # TC : O(N)
    # SC : O(N)
    def findKthPositive(self, arr: List[int], k: int) -> int:

        arr = set(arr)
        
        for i in range (1000001):
            if i not in arr:
                k-=1
                if k==-1:
                    return i
    

    def findKthPositive(self, arr: List[int], k: int) -> int:
        start , end = 0 , len(arr)

        while start < end :
            pass
    
        