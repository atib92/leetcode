'''
86. Partition List
Solved
Medium
Topics
conpanies icon
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        The idea is pretty simple:
        We concurrently maintain a smaller and larger linkedlist depending on the value of the current node's value.
        * We use senitel smaller and larger heads to not handle edge cases (First smaller/larger node, no smaller/larger node, etc..)
        * Detach: We are not detaching nodes while concurrently building the larger and smaller linked lists since we know the prev pointer
                  will be finally rewritren (detached) in the future. This means we have to do an explicit larger_current.next = None. One
                  could do the detach during the concurrent creation of the lists also.
        '''
        head_smaller = ListNode()
        head_larger = ListNode()
        smaller_current = head_smaller
        larger_current = head_larger
        current = head
        while current is not None:
            if current.val < x:
                smaller_current.next = current
                smaller_current = smaller_current.next
            else:
                larger_current.next = current
                larger_current = larger_current.next
            current = current.next
        smaller_current.next = head_larger.next
        larger_current.next = None
        return head_smaller.next
