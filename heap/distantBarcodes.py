# https://leetcode.com/problems/distant-barcodes/

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        c = Counter(barcodes)
        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)

        result = []

        c1, k1 = 0, 0
        c2, k2 = 0, 0

        while heap:

            if heap:
                c1, k1 = heapq.heappop(heap)
                result.append(k1)
                c1+=1
            if heap:
                c2, k2 = heapq.heappop(heap)     
                result.append(k2)
                c2+=1
            
            if c1 < 0:
                heapq.heappush(heap, (c1, k1))
            if c2 < 0:
                heapq.heappush(heap, (c2, k2))
            

        return result