from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        if fast:
            fast = fast.next

        while fast.next:
            tmp = slow.val
            slow.val = fast.val

            if slow.next:
                slow.next.val = tmp
                slow = slow.next

            if fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next

        return head


Solution().swapPairs(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
)
