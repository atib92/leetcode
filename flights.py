"""
Given an origin airport, destination airport, and series of flights determine whether it is possible for a package at the origin to reach the destination. A flight is represented as departure airport, arrival airport, departure time, and arrival time.
During the transportation, the time that the package leaves the airport needs to be greater than or equal to the time it arrives at the airport. Please determine whether it is possible for a package transfer from s to t. The package arrived at s at time 0.

E.g. 1
Origin: "NYC"
Destination: "SFO"
Flights: NYC → LAX, Departure: 0, Arrival: 4
LAX - SFO, Departure: 5, Arrival: 7
Output: True

E.g 2
Origin: "NYC" Destination: "SFO"
Flights: NYC →> LAX, Departure: 0, Arrival: 4
LAX -> SFO, Departure: 3, Arrival: 5
Output: False
"""

"""
Algo:
    1. Lets denote airports by integer indexes : 0,1,2... (These can be enums or some class variables when we design the system).
    2. Graph creation:
        a. Each airport is basically a node
        b. Each edge in the graph is a flight represented as (t1,t2) e.g: (3,7):
           such that   t1: Departure time of the flight from the current node.
                       t2: Arrival time of the flight at the adjacent node.
        c. Traversal: We introduce a concept of current time starting at 0 from the SRC airport and try to traverse (DFS/BFS)
           from the SRC airport. An adjance node/airport will only be traversed (recursively/enqueued) if t_now <= edge[0] and
           if yes, t_now will be updated as t_now = edge[1] (Note: timestamps in the edges are absolute times and not durations.)
           If by doing this we reach the DST we have succeeded.
"""
from collections import deque


NYC = 0
LAX = 1
SFO = 2

adj = [[None, (0,4), None],
       [None, None, (5,7)],
       [None, None, None]]

def bfs(src, dst):
    num = 0
    q = deque()
    q.append((src,0,[])) # airport, t_now and airports to avoid (basically previously visted airports so that we do not go in loops.)
    while(len(q) > 0):
        airport, t_now, avoid = q.popleft()
        if airport == dst:
            #return True, t_now
            print('Reached {} at {}'.format(dst, t_now))
            num += 1
        else:
            for next_airport, flight in enumerate(adj[airport]):
                if flight is not None and next_airport != airport and next_airport not in avoid:
                    if t_now <= flight[0]:
                        avoid.append(airport)
                        q.append((next_airport, flight[1], avoid))
    return num


times = bfs(NYC, SFO)
print(times)
