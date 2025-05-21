"""
HACKERRANK 
Markov takes out his Snakes and Ladders game, stares at the board and wonders: "If I can always roll the die to whatever number I want, what would be the least number of rolls to reach the destination?"

Rules The game is played with a cubic die of  faces numbered  to .

Starting from square , land on square  with the exact roll of the die. If moving the number rolled would place the player beyond square , no move is made.

If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.

If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.

Function Description

Complete the quickestWayUp function in the editor below. It should return an integer that represents the minimum number of moves required.

quickestWayUp has the following parameter(s):

ladders: a 2D integer array where each  contains the start and end cell numbers of a ladder
snakes: a 2D integer array where each  contains the start and end cell numbers of a snake
Input Format

The first line contains the number of tests, .

For each testcase:
- The first line contains , the number of ladders.
- Each of the next  lines contains two space-separated integers, the start and end of a ladder.
- The next line contains the integer , the number of snakes.
- Each of the next  lines contains two space-separated integers, the start and end of a snake.

Constraints



The board is always  with squares numbered  to .
Neither square  nor square  will be the starting point of a ladder or snake.
A square will have at most one endpoint from either a snake or a ladder.

Output Format

For each of the t test cases, print the least number of rolls to move from start to finish on a separate line. If there is no solution, print -1.

Sample Input

2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21 
Sample Output

3
5

"""
from collections import deque

def quickestWayUp(ladders, snakes):
    """
    1. Create a hash for quick lookup of src, dst for ladders and snakes
    2. Traverse using BFS
    3. Mark visited nodes (using sets for faster membership checks)
    4. Early exit if you reach the destinatino
    5. Return -1 if cannot reach

    Why not DFS: DFS would also work with similiar visited marking, its just that stopping all other recursions/paths when a path
    reaches a destination requires storing a global variable, e.g "done". BFS seems cleaner. Plus safer since there is not risk
    of infinite recursions.
    """
    l_hash, s_hash = {}, {}
    for ladder in ladders:
        l_hash[ladder[0]] = ladder[1]
    for snake in snakes:
        s_hash[snake[0]] = snake[1]
    visited = set()
    q = deque()
    q.append((1,0)) # (current_cell, number_of_rolls_so_far)
    while(len(q) != 0):
        cell, rolls = q.popleft()
        #print(f'cell {cell} rolls {rolls} visited {visited}')
        if cell == 100:
            return rolls
        elif cell > 100 or cell in visited:
            pass
        elif cell in l_hash:
            visited.add(cell)
            q.append((l_hash.get(cell) ,rolls))
        elif cell in s_hash:
            visited.add(cell)
            q.append((s_hash.get(cell), rolls))
        else:
            visited.add(cell)
            for roll in range(6,0,-1):
                q.append((cell + roll, rolls+1))
    return -1
