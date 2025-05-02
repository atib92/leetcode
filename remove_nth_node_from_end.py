"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    The idea is very simple. The last node is the first node from the end, the second last node is the 2nd node from end...
    i,e we we keep a slow and fast pointer and first move the first pointer by n-1 and then move both pointer together, when
    the fast pointer reaches the last node, the slow pointer will be point to the node to be delted. After that, its just a
    matter of rearraing the pointers and taking care of the case when the node to be deleted is the head of the node.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_ptr = slow_ptr = head
        step = n-1
        while(step != 0):
            step -= 1
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
        prev_ptr = None
        while(fast_ptr and fast_ptr.next is not None):
            fast_ptr = fast_ptr.next
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
        # Now slow_ptr points to the node to be deleted
        if prev_ptr is not None:
            prev_ptr.next = slow_ptr.next
        else:
            head = slow_ptr.next
        return head
