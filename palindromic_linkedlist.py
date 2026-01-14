'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        TIme O(n)
        Space O(n)
        '''
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        node = head
        while node:
            if node.val != stack.pop():
                return False
            node = node.next
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Time O(n)
        Space O(1)
        Pass 1 - Reverse the first half of the linkedlist.
        Pass 2 - Start comparing the reverse first half with the remaining second half (Take care of skipping the mid point of odd length linked lists)
        '''
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        # Now n is the length of the palindrome 
        mid_point = n // 2
        l = 0
        node = head
        prev = None
        while node:
            l += 1
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            start_reverse, start_forward = None, None
            if l == mid_point:
                start_reverse = prev
                if n % 2 != 0:
                    # odd
                    start_forward = node.next
                else:
                    start_forward = node
                break
        while start_forward and start_reverse:
            if start_forward.val != start_reverse.val:
                return False
            else:
                start_forward = start_forward.next
                start_reverse = start_reverse.next
        return True
            
