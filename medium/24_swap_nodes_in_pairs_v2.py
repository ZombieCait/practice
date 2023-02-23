"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = left = head

        if right:
            right = right.next

        while right:
            tmp = right.val
            right.val = left.val
            left.val = tmp

            if right.next:
                right = right.next.next
                left = left.next.next
            else:
                right = right.next

        return head


l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution().swapPairs(l)

while solution:
    print(solution.val)
    solution = solution.next
