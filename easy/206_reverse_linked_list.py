"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
----------
speed
O(n)

memory
O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            head.next = head.val
            head.val = head.next.val

            head = head.next
