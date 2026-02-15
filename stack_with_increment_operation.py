'''
Design a Stack With Increment Operation
Solved
Medium
Topics
conpanies icon
Companies
Hint
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
 

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.
 

Constraints:

1 <= maxSize, x, k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
'''


class CustomSimpleStack:
    '''
    Push O(1)
    Pop O(1)
    Incr O(k)
    '''
    def __init__(self, maxSize: int):
        self._stack = []
        self._size = 0
        self._capacity = maxSize

    def push(self, x: int) -> None:
        if self._size < self._capacity:
            self._size += 1
            self._stack.append(x)

    def pop(self) -> int:
        if self._size > 0:
            self._size -= 1
            return self._stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        #print(f'k:{k} val:{val} size:{self._size}\n {self._stack}')
        for index in range(min(self._size, k)):
            self._stack[index] += val

class CustomStack:
    '''
    LAZY INCREMENT
    delegage increment to when the element is popped.
    The key observation is when incr(k, v) is done, it needs
    to add k to all elements from index 0 to k-1 but pop always
    happens from the top so we can store the net "to add" at index
    k-1 and lazily add during the pop operation, but also pass it
    down after pop.
     0  1  2  3   4
    [10 11 12 13 14]
    incr(2, 10)
    [10 11 12 13 14] -> [20 21 12 13 14]
    [0  10  0  0  0]
    incr(3, 10)      -> [30 31 22 13 14]
    [0 10  10  0  0]
    pop()
    [10 11 12 13]
    [0  10 10 0 ] <No change since the tos didn't have any inc stored>
    pop()
    [10 11 12]
    [ 0 10 10]
    pop() -> 22
    [10 11]
    [0 20]
    '''
    def __init__(self, maxSize: int):
        self._stack = []
        self._size = 0
        self._capacity = maxSize
        self._addition = [0] * self._capacity

    def push(self, x: int) -> None:
        if self._size < self._capacity:
            self._size += 1
            self._stack.append(x)

    def pop(self) -> int:
        if self._size > 0:
            value = self._stack.pop()
            addon = self._addition[self._size - 1]
            self._addition[self._size-1] = 0 # Important cleanup !
            self._size -= 1
            if self._size > 0:
                self._addition[self._size - 1] +=  addon
            return value + addon
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self._size > 0:
            self._addition[min(k, self._size)-1] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)