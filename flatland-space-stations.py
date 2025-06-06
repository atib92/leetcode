"""
HACKERRANK
Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of  length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station.

Example
n = 3
c = [1]


There are 3 cities and city 1 has a space station. They occur consecutively along a route. City 0 is 1 unit away and city 2 is 1 units away. City 1 is 0 units from its nearest space station as one is located there. The maximum distance is 1.

Function Description

Complete the flatlandSpaceStations function in the editor below.

flatlandSpaceStations has the following parameter(s):

int n: the number of cities
int c[m]: the indices of cities with a space station
Note: There will be atleast 1 city with a space station
"""
def flatlandSpaceStations(n, c):
    """
    Cities : 0----1----2----3----4--...--n-1
    c[i] : city with a space station
    Algo: Multi Pass Approach:
    1. Start from city-0 till city-n-1 and update L[]
       s.t L[i] is the closest distance to city with
       a space station from the left
    2. Start from city-n-1 till city-0 and update R[]
       s.t R[i] is the closest distance to city with
       a space station from the right
    Third Pass:
    ans = max(ans, min(L[i], R[i]))
    """
    L = [float("inf")] * n
    R = [float("inf")] * n
    for _, city_index in enumerate(c):
        L[city_index] = 0
        R[city_index] = 0
    for city_index in range(1, n):
        L[city_index] = min(L[city_index], 1+L[city_index-1])
    for city_index in range(n-2,-1,-1):
        R[city_index] = min(R[city_index], 1+R[city_index+1])
    max_distance = 0
    for city_index in range(n):
        max_distance = max(max_distance, min(L[city_index], R[city_index]))
    return max_distance
