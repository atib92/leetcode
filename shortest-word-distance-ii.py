"""
Shortest Word Distance II
Solved
Medium
Topics
conpanies icon
Companies
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""
class WordDistance:
    """
    The idea is pretty simple, we will maintain a sorted list of indices alongside of each word and whenever asked to compare 2 words we will run a "dry merge"
    (similar to the merge of mergesort, "dry" because we are not really storing the merged array) of the two array.
    Merge: track indices in the two arrays by i and j. Compare the difference in values and update the min if required, them move the index which is pointing
    to the smaller element.
    """
    def __init__(self, wordsDict: List[str]):
        self.map = {}
        for index, word in enumerate(wordsDict):
            if word in self.map:
                self.map[word].append(index)
            else:
                self.map[word] = [index]
    def minDiff(self, arr_a, arr_b):
        # DRY MERGE !
        i, j, m, n = 0, 0, len(arr_a), len(arr_b)
        min_diff = float("inf")
        while(i < m and j < n):
            min_diff = min(min_diff, abs(arr_a[i] - arr_b[j]))
            if arr_a[i] < arr_b[j]:
                i += 1
            else:
                j += 1
        return min_diff
     
    @cache
    def shortest(self, word1: str, word2: str) -> int:
        a = self.map[word1]
        b = self.map[word2]
        return self.minDiff(a, b)      


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
