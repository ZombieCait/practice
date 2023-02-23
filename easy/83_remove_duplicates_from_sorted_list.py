"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
---------------
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
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return_sorted = result = ListNode(-200)
        while head:
            if head.val == result.val:
                head = head.next
                if head == None:
                    result.next = None

            else:
                result.next = head
                result, head = result.next, head.next

        return return_sorted.next


a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
Solution().delete_duplicates(a)
