# https://leetcode.com/problems/number-of-recent-calls

class RecentCounter:

    # TC : O(N)
    # SC : O(N)

    def __init__(self):
        self.record = deque([])

    def ping(self, t: int) -> int:


        # Design choice to use queue is because we do not want keep expired records in memory
        # We can also maintain a count for pops and appends to save on len() traversal 

        self.record.append(t)
        while self.record and self.record[0] < t-3000:
            self.record.popleft()
        return len(self.record)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)