'''
 Design Circular Queue
Solved
Medium
Topics
conpanies icon
Companies
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
'''

'''
Algorithm:
We will use the producer consumer construct of circular buffers.
We have two pointers in and out. in is where the producer produces objects (enque operation)
and out is from where the consumer consume (deque operation)

in, out = 0, 0
Full Criteria: No place for producer to produce i,e (in + 1) % size == out
Empty Criteria: Nothing for the consumer to consume in == out

Note: size here is 1 more than the buffer size. We waste one space to be able to detect the full criteria cleanly
'''
class MyCircularQueue:

    def __init__(self, k: int):
        '''
        out....in
        Elements are produced (enqueued) at in
        Elements are consumed (dequeued) from out
        empty: in == out
        full: (in+1)%k == out
        '''
        self.k = k+1
        self.q = [None] * self.k
        self.inptr, self.outptr = 0, 0 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.inptr] = value
            self.inptr = (self.inptr + 1) % self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            #val = self.q[self.outptr]
            self.outptr = (self.outptr + 1) % self.k
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.outptr]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[(self.inptr-1)%self.k]

    def isEmpty(self) -> bool:
        return self.inptr == self.outptr

    def isFull(self) -> bool:
        return (self.inptr + 1) % self.k == self.outptr


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


'''
Concurrent Version: 
In the concurrent version enque and deque operations can step on each other, so we will use
locks. 
a. We need one lock to synchronize operations on the critical section (the buffer). This can be a simple Mutex
b. We need to syncronise between the enque and deque operations to signal the availability of empty slots in the
   buffer and the availibility of objects to be consumed. For this we will use 2 Semaphors

Semaphores:
    s_empty = Semaphore(BUFFER_SIZE)
    s_full = Semaphore(0)
Mutes:
    b_lock = Mutex()


 # Producer
    wait(s_empty)
    acquire(b_lock)
    produce()
    release(b_lock)
    signal(s_full)

# Consumer
    wait(s_full)
    acquire(b_lock)
    consueme()
    release(b_lock)
    signal(s_empty)
'''