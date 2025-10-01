"""
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Constraints:

1 <= target, startFuel <= 109
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 10^9

"""
import heapq
class Solution:
    """
    Intuition: We keep on cumulatively adding fuel to ensure cumulative fuel >= distance
    At any time reach a gas station with cumulative fuel >= distance, we do not to immediate refill, so we push to a queue and continue.
    If cumulative fuel < distance, we try to greedily pick the best gas refills until fuel becomes >= distance.
    By doing this we can reach the end, we are good. At any point we run out of fuel we return -1
    For greedily picking the best gas stations, we use a max heap
    Time : NlogN, each gas station is enqueue and dequeued once
    """
    def minRefuelStops_Working(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        fuel = start_fuel
        count = 0
        gas = [] # max heap
        for distance, refill in stations:
            while(gas and fuel < distance):
                fuel += -1*heapq.heappop(gas)
                count += 1
            if fuel < distance:
                # Car cannot reach desitinatin
                print(f'Car cannot reach dest. Should not happen')
                return -1
            # Don't refill but remember
            heapq.heappush(gas, -1*refill)
        while(gas and fuel < target):
            fuel += -1*heapq.heappop(gas)
            count += 1
        if fuel < target:
            return -1
        else:
            return count

    def minRefuelStops(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        """
        Cleaner version !
        """
        fuel = start_fuel
        count = 0
        gas = [] # max heap
        stations.append([target, 0]) # This makes it cleaner
        for distance, refill in stations:
            while(gas and fuel < distance):
                fuel += -1*heapq.heappop(gas)
                count += 1
            if fuel < distance:
                return -1
            heapq.heappush(gas, -1*refill)
        return count
