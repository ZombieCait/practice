from copy import copy
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_linked_list(self, head):
        reversed = ListNode(head.val)

        while head.next:
            next = head.next
            reversed = ListNode(next.val, reversed)
            head = head.next

        return reversed

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_head = self.reverse_linked_list(copy(head))

        while reversed_head:
            if reversed_head.val != head.val:
                return False
            
            reversed_head = reversed_head.next
            head = head.next
            
        return True

list_node = ListNode(1, ListNode(7, ListNode(7, ListNode(1))))

print(Solution().isPalindrome(list_node))