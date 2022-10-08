# https://leetcode.com/problems/my-calendar-i/

from sortedcontainers import SortedList
import bisect

class MyCalendar:


    # TC : O(NlogN)
    # SC : O(N)
    
    def __init__(self):
        self.calendar = SortedList()        

    def book(self, start: int, end: int) -> bool:

        ind = bisect.bisect_left(self.calendar, [start, end])
        if (ind > 0 and self.calendar[ind-1][1]>start) or (ind<len(self.calendar) and  end> self.calendar[ind][0]):
            return False
        
        self.calendar.add([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)