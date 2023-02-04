from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def len(self, head):
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next
        return cnt

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.len(head)
        
        if length % 2 == 0:
            middle = int(length / 2) + 1
        middle = int(length / 2)

        result = head
        while middle != 0:
            result = result.next
            middle = middle - 1
        return result


list_node = ListNode(1, ListNode(7, ListNode(7, ListNode(1))))

print(Solution().middleNode(list_node))