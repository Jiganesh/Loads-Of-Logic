
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:

        dictionary = Counter(s)
        heap = [ [-v, k] for k , v in dictionary.items()]
        heapq.heapify(heap)

        result = ""
        previous = None

        while heap or previous:

            if not heap and previous:
                return ""

            count, ch = heapq.heappop(heap)
            result += ch
            count += 1

            if previous :
                heapq.heappush(heap, previous)
                previous = None
            
            if count != 0:
                previous = [count, ch]

        return result