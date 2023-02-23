"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        result = sorted_res = ListNode()

        while list1 and list2:
            if list2.val >= list1.val:
                result.next = list1
                list1, result = list1.next, result.next

            else:
                result.next = list2
                list2, result = list2.next, result.next

        if list1 or list2:
            result.next = list1 if list1 else list2

        return sorted_res.next


a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(5)))

Solution().merge_two_lists(a, b)
