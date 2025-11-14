"""
Maximum Frequency Stack
Solved
Hard
Topics
conpanies icon
Companies
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""
class FreqStack:
    """
    Store a stack of elements per count i.e a stack of elements for count=10 for all elements that occurs 10 times.
    Maintain a map of elements to its freqency (so that we can access the right stack)
    Maintain the maximum count seen thus far
    Push : Find the current count of the number and inc that by 1. Append the element to the incremented count's stack. (Note: The element also exists in the older count's stack)
    PopMax: Pop the TOS from the max count's stack. If the max count's stack stil has elements in it, we are good else delete that count's stack and update max count. Also update
            the map to indicate where the value now resides
    """
    def __init__(self):
        self._freq = {} # counter:[]
        self._map = {}  # val:count
        self._max_freq = 0

    def push(self, val: int) -> None:
        if val in self._map:
            count = self._map.get(val)
        else:
            count = 0
        count += 1
        self._map[val] = count
        
        self._max_freq = max(self._max_freq, count)
        
        if count in self._freq:
            self._freq[count].append(val)
        else:
            self._freq[count] = [val]

    def pop(self) -> int:
        if self._max_freq in self._freq:
            val = self._freq[self._max_freq].pop()
            if not self._freq[self._max_freq]:
                del self._freq[self._max_freq]
                self._max_freq -= 1
            self._map[val] -= 1
            if self._map[val] == 0:
                del self._map[val]
            return val
        else:
            return None


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
