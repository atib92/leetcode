"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

"""
class Solution:
    """
    We use something very similar to the knapsack top down DP approach.
    We maintain a DP matrix where columns run from w=0 to w=target i,e w+1 columns and rows run from 0 to len(candidates) i,e N+1 rows. The extra row padding (row=0) helps us freely checking dp[i-1][w] w.o the extra i > 0 check.

    Building the DP matrix bottoms up:
    dp[i][w] is basically going to contain all possible combinations that sums up to target w using indices from 0 to i-1. Everthing is initialized to None but dp[*][0] is initialized to [] to bootstrap the process.
    dp[i][w] can be populated using:
    1. dp[i-1][w] : I,e all the ways we could already hit the target w using the candiates before i.
    2. dp[i][w-candidates[i-1]]: All ways we could hit target w-current_val using the candidates before i. Note: we have padded an extra row so ith row in dp matrix actually is the i-1th index in the candidate matrix.

    if dp[i-1][w] returns [[A,B], [C,D,E]] : We can add this to the results of dp[i][w]
    if dp[i][w-candidates[i-1]] returns [[F,G], [H,I,G]] : we can add [[F,G, v], [H,I,G,v]] where v is candiates[i-1] i,e the current element.

    if any of the both return None, we maintain dp[i][w] as None

    Why sort the candidates ?
    Sorting the candidates helps avoid redudant combinatios like [2,1] and [1,2]. If the array is sorted, and prev results are [2,2], we can never add a smaller element in subsequent rows so we will never try [2,1].
    """
    def combinationSum2_topDownDP(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        N = len(candidates)
        dp = [ [None] * (target+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0]= []
        for i in range(1, N+1):
            for t in range(1, target+1):
                #print(f'i:{i} t:{t}')
                results = []
                # Take
                if t - candidates[i-1] >= 0 and dp[i-1][t - candidates[i-1]] != None:
                    if dp[i-1][t - candidates[i-1]] == []:
                        results.append([candidates[i-1]])
                    else:
                        for combination in dp[i-1][t - candidates[i-1]]:
                            results.append(combination + [candidates[i-1]])
                # Skip
                if dp[i-1][t] != None:
                    for combination in dp[i-1][t]:
                        if combination not in results:
                            results.append(combination)
                if results == []:
                    dp[i][t] = None
                else:
                    dp[i][t] = results
        return dp[N][target] or []
