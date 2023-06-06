# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mappings = [0]*(n+1)

        for first , last , seats in bookings:
            print(first, last, seats)
            mappings[first-1]+= seats
            mappings[last] -= seats

        prefix_sum = list(accumulate(mappings, operator.add))
        prefix_sum.pop()
        return prefix_sum
        