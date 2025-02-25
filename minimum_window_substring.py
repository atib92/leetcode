""" 
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string.
"""
class Solution:
    """ 
    Algo: Start from the left and keep on going to the right until the criteria is met.
          Start popping element from the left and continously keep checking if criteria is still met. If yes, you are finding a better / smaller substring.
          Once the criteria fails, resume adding elments to the right until criteria is met. 
          Repeat !
          This is O(n+m)
    """
    def minWindow(self, s: str, t: str) -> str:
        desired = {}
        need = len(t)
        for char in t:
            if char not in desired:
                desired[char] = 1
            else:
                desired[char] += 1
        current = {}
        for char in desired:
            current[char] = 0
        have = 0
        start = 0
        window = 100000
        out = ""
        for index, char in enumerate(s):
            if have < need:
                # Substring not yet formed so keep looking
                if char in t:
                    if current[char] < desired[char]:
                        have += 1
                    current[char] += 1
                    if have >= need:
                        # have >= need so we can try to find a smaller window
                        while(have >= need):
                            new_window = (index) - (start) + 1
                            if new_window < window:
                                # print(f's {s} Window start {start} end {index} string {s[start:index+1]}')
                                window = new_window
                                out = s[start:index+1]
                            start_char = s[start]
                            if start_char in t:
                                current[start_char] -= 1
                                if current[start_char] < desired[start_char]:
                                    have -= 1
                            start += 1
        return out
