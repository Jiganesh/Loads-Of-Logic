# https://leetcode.com/problems/largest-values-from-labels/

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:


        c = {label: useLimit for label in labels}

        heap = [(-k,v) for k, v in list(zip(values, labels))]

        heapq.heapify(heap)
        
        result = 0

        while heap and numWanted > 0 :
            mv , ml = heapq.heappop(heap)
            if c[ml] > 0:
                c[ml]-=1
                result += mv
                numWanted -= 1

        return -result