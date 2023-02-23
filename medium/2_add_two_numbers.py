"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
---------------
speed
O(n)

memory
O(n)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        number1 = ""
        number2 = ""
        while l1 or l2:
            try:
                number1 = str(l1.val) + number1
                l1 = l1.next
            except:
                pass

            try:
                number2 = str(l2.val) + number2
                l2 = l2.next
            except:
                pass

        result = str(int(number1) + int(number2))
        l_result = ListNode(int(result[0]))

        for i in list(str(result))[1:]:
            l_result = ListNode(int(i), l_result)

        return l_result


l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
solution = Solution().addTwoNumbers(l1, l2)
while solution:
    print(solution.val)
    solution = solution.next
