'''
Design Hit Counter
Solved
Medium
Topics
conpanies icon
Companies
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
 

Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
 

Follow up: What if the number of hits per second could be huge? Does your design scale? <<<< ---------------- IMPORTANT --------------------<
'''

from collections import deque

class HitCounterBaseic:
    '''
    Basic deque for storing timestamps.
    Assumption: Timestamps are monotonically increasing.
    Pros: Simple
    Cons: Memory Intensive
    '''
    def __init__(self):
        self.hits = deque()
        self.n = 0

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.n += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.n -= 1
            self.hits.popleft()
        return self.n

class HitCounter:
    '''
    Use a circular buffer with 300 slots.
    Space and Time: O(1)
    Pros:
    i. Works if timestamps are not monotonic
    ii. Works at large scale
    '''
    def __init__(self):
        self.timestamp = [0] * 300 # 300 slots for 300 seconds
        self.count = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.timestamp[idx] <= timestamp - 300:
            self.count[idx] = 1
        else:
            self.count[idx] += 1
        self.timestamp[idx] = timestamp

    def getHits(self, timestamp: int) -> int:
        count = 0
        for idx in range(300):
            if self.timestamp[idx] > timestamp - 300:
                count += self.count[idx]
        return count



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)



