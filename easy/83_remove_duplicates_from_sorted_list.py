
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return_sorted = result = ListNode(-200)
        while head:
            if  head.val == result.val:
                head = head.next
                if head == None:
                    result.next = None

            else:
                result.next = head
                result, head = result.next, head.next

        return return_sorted.next

a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
Solution().deleteDuplicates(a)