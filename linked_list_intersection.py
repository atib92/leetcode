"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Naive Solution : The first solution that comes to mind is to traverse the first linkedlist and mark every node as visited and then traverse the second list, if during
                     the traversal of the second linkedlist, we encounter a node that is already visited, that is the intersection node.
                     However its a bit naive to assume we can change (or even have access to) the internal data structure of the linkedlist (for visited marking). In this
                     alog, if we do not have access to the node's internal memeber, we will have to store some kind of visited list of node's address and an in the second
                     traversal, check if a node is alreay there in the visited cache which makes the problem O(N*M).

    Optimal Solution: The key to a linear solution is observing this. If we can determine the longer and the shorter linked list and measure the difference in length, we
                      can traverse the longer linkedlist by the offset first. Now if we concurrently traverse botht the linkedlists, we can be sure that we will end up
                      on the intersection node at the same time. 
                      Note: We do not require any access to the node's data.
    """
    def _length(self, head: ListNode):
        if head is None:
            return 0
        else:
            return 1 + self._length(head.next)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        L1, L2 = self._length(headA), self._length(headB)
        if L1 >= L2:
            longer, shorter = headA, headB
        else:
            longer, shorter = headB, headA
        delta = abs(L1 - L2)
        while(delta > 0):
            longer = longer.next
            delta -= 1
        while(longer is not None and shorter is not None):
            if longer is shorter:
                return longer
            else:
                longer = longer.next
                shorter = shorter.next
        return None
        
