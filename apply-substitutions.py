"""
Apply Substitutions
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given a replacements mapping and a text string that may contain placeholders formatted as %var%, where each var corresponds to a key in the replacements mapping. Each replacement value may itself contain one or more such placeholders. Each placeholder is replaced by the value associated with its corresponding replacement key.

Return the fully substituted text string which does not contain any placeholders.

 

Example 1:

Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"

Output: "abc_def"

Explanation:

The mapping associates "A" with "abc" and "B" with "def".
Replace %A% with "abc" and %B% with "def" in the text.
The final text becomes "abc_def".
Example 2:

Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"

Output: "bce_ace_abcace"

Explanation:

The mapping associates "A" with "bce", "B" with "ace", and "C" with "abc%B%".
Replace %A% with "bce" and %B% with "ace" in the text.
Then, for %C%, substitute %B% in "abc%B%" with "ace" to obtain "abcace".
The final text becomes "bce_ace_abcace".
 

Constraints:

1 <= replacements.length <= 10
Each element of replacements is a two-element list [key, value], where:
key is a single uppercase English letter.
value is a non-empty string of at most 8 characters that may contain zero or more placeholders formatted as %<key>%.
All replacement keys are unique.
The text string is formed by concatenating all key placeholders (formatted as %<key>%) randomly from the replacements mapping, separated by underscores.
text.length == 4 * replacements.length - 1
Every placeholder in the text or in any replacement value corresponds to a key in the replacements mapping.
There are no cyclic dependencies between replacement keys.
"""
from collections import deque

class Solution:
    """
    1. Build topological order from replacements
    2. Resolve in that order
    """
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        values = {}
        adj = {}
        indeg = {}
        for key, _ in replacements:
            # We go through the keys so that the adj and indeg processing becomes simpler.
            values[key] = value
            adj[key] = set()
            indeg[key] = 0
        for key, value in replacements:
            l, i = len(value), 0
            while(i < l):
                if value[i] == "%":
                    src = value[i+1]
                    if key not in adj[src]:
                        adj[src].add(key)
                        indeg[key] += 1
                    i += 3
                else:
                    i += 1
        q = deque()
        # Go over indge and start with the ones with 0 indeg
        for var, count in indeg.items():
            if count == 0:
                q.append(var)
        toplogical_order = []
        while(q):
            var = q.popleft()
            toplogical_order.append(var)
            for dst in adj[var]:
                indeg[dst] -= 1
                if indeg[dst] == 0:
                    q.append(dst)
        for var in toplogical_order:
            resolved_value = ""
            value = values[var]
            l, i = len(value), 0
            while(i < l):
                if value[i] == "%":
                    src = value[i+1]
                    resolved_value += values[src]
                    i += 3
                else:
                    resolved_value += value[i]
                    i += 1
            values[var] = resolved_value
        res = ""
        l, i = len(text), 0
        while(i < l):
            if text[i] == "%":
                var = text[i+1]
                res += values[var]
                i += 3
            else:
                res += text[i]
                i += 1
        return res
