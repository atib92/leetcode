"""
 Rotate List
Solved
Medium
Topics
conpanies icon
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def util(self, head):
        prev, node, n = None, head, 0
        while(node):
            n += 1
            prev = node
            node = node.next
        return prev, n
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            <---n-k--><--k-->
        head ............ tail
        If you think about the rotatation, its basically taking the last k elements
        moving it to the front.
        1. Normalize k by mod division with n so that you do not go round the linked list more than once
        2. Find n-k from the front: This is the new tail
        3. Move everthing after the new tail to the front.
        """
        if not head :
            return head
        tail, n = self.util(head)
        k = k % n
        node = head
        step = 1
        while(node and step < n-k):
            node = node.next
            step += 1
        tail.next = head
        head = node.next
        node.next = None
        return head
