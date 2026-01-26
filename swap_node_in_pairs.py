
'''
Swap Nodes in Pairs
Solved
Medium
Topics
conpanies icon
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Simple recursive approach.
        Note: A similar iterative approach can also be used by using a while loop on node and node.next.
        like this: 
        while node and node.next:
            ...

        '''

        def _swap(prev, node):
            if node is None or node.next is None:
                return
            else:
                prev.next = node.next
                third = node.next.next
                node.next.next = node
                node.next = third
                _swap(node, third)

        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        _swap(prev, head)
        return dummy.next