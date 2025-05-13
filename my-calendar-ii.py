"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""
from sortedcontainers import SortedDict


class MyCalendarTwo:
    """
    Brute Force: Store all bookings in the format (startTime, endTime) and then for each new booking:
    i. Find out all bookings that overlap with this new booking, calling this the overlapping_bookings_list
    ii. Iterate over the overlapping_bookings_list using 2 for loops and check if any two overlaps among themselves. 
    If that's the case, you the new booking will result into a TRIPLE BOOKING and hence must be reject.

    Time: O(N^2) : Because of the nest for loop. Won't work at scale.

    Better Solution: LINE SWEEP
    The idea is to be able to find the no of booking in any time range and check if the new booking will result
    into an Triple Booking.
    1. Store start and end times in a sorted map. map[start] and map[end] will store the 'net' booking starting at that time.
    2. For every booking, we just need to iterate over the map and keep a count of how many bookings are ongoing at any point of time.
    3. When we are inside the new booking range, if we hit the TRIPLE BOOKING condition, we return False.

    THE LINE SWEEP ALGORITHM WORKS IRRESPECTIVE OF WHATEVER THE VALUE OF MAX BOOKINGS (3 in this question) ARE.
    """
    def print(self, s):
        pass

    def __init__(self):
        self._map = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self._map[startTime] = self._map.get(startTime, 0) + 1
        self._map[endTime] = self._map.get(endTime, 0) - 1
        ongoing = 0
        for t, val in self._map.items():
            # The t >= endTime is an early exit condition. The code works even w/o it but early exit improves the overall run time.
            # since once we are outside the new booking time range, there is no point in continuing.
            if t >= endTime:
                break
            if ongoing == 3:
                # We are goig to revert the changes to the amp since this booking is not going to be entertained.
                self._map[startTime] -= 1
                if self._map[startTime] == 0:
                    del self._map[startTime]
                self._map[endTime] += 1
                if self._map[endTime] == 0:
                    del self._map[endTime]
                return False
        return True
