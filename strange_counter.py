"""
There is a strange counter. At the first second, it displays the number 3. Each second, the number displayed by decrements by 1 until it reaches 1. 
In next second, the timer resets to 2*initial number in the previous cycle and continues counting down. The diagram below shows the counter values for each time  in the first three cycles:

Find and print the value displayed by the counter at time .

Function Description

Complete the strangeCounter function in the editor below.

strangeCounter has the following parameter(s): int t: an integer
Returns int: the value displayed at time t
Input Format :A single integer, the value of t.
t < 10^12
"""

def strangeCounter(t):
    """
    Since t can be 10^12, brute force won't work here. We use a greedy approach
    1. Hop over all "double" cycles 
    2. Adjust for the remaining decrements
    """
    now = 1
    start = 3
    value = 3
    while(now + start <= t):
        now += start
        value = 2*start
        start = value
    return value - (t-now)
