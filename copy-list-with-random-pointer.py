"""
Copy List with Random Pointer
Solved
Medium
Topics
conpanies icon
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""


# Solution 1 : Using Extra Space for hash
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        We will maintain a hash orig_node_ptr:copy_node_ptr
        1. Traverse the linked list and create the duplicate linked list with Null random pointer
        2. Do a second pass and use :
           i.  Its duplicate : dup_node = hash[node]
           ii. Its random ptr : node.random
           iii. Copy of the random pointeed node dup_random_node = hash[node.random]
           SET: dup_node.random = dup_random_node
        """
        if head is None:
            return None
        else:
            node_hash = {}
            parent = None
            dup_parent = None
            node = head
            dup_head = None
            while(node is not None):
                dup_node = Node(node.val, next=None, random=None)
                node_hash[node] = dup_node
                if dup_parent is not None:
                    dup_parent.next = dup_node
                else:
                    dup_head = dup_node # Return this finally
                dup_parent = dup_node
                parent = node
                node = node.next
            # Second pass
            node = head
            while(node is not None):
                dup_node = node_hash[node]
                dup_node.random = node_hash.get(node.random)
                node = node.next
            return dup_head

# Solution 2: Using interleaving and no extra hash
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        A->A_bar->B->B_bar->C->C_bar
        Now say A---random--->-----C
        then, access A's dup i,e A_bar as A->next
                     A's random pointer i,e C as A->random
                     C's dup as A->random->next
                     and set:
                     A->next->random = A->random->next !!!
        Finally undo the interleaving !
        """
        node = head
        duplicate_head = None
        while(node):
            duplicate_node = Node(node.val, node.next)
            node.next = duplicate_node
            node = duplicate_node.next
            if duplicate_head is None:
                duplicate_head = duplicate_node
        # Now set the random pointers
        node = head
        while(node):
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        # Undo Interleaving
        node = head
        while(node and node.next):
            temp = node.next
            node.next = node.next.next
            node = temp
        return duplicate_head
