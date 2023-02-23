'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

spped O(n)
memory O(1)
'''

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        while head:
            if 'i' in str(head.val):
                return head

            head.val = 'i' + str(index)
            head = head.next
            index += 1

        return head

class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        while head != slow:
            head, slow = head.next, slow.next
        return head

list_node = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))

print(Solution2().detectCycle(list_node))
