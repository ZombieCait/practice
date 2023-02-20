from typing import Optional

'''
[1, 2, 3, 4, 5, None] -> [5, 4, 3, 2, 1, None]

O(n)
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        current = head
        
        while current:
            next_node = current.next
            current.next = result
            result = current
            current = next_node
            

        return result


            