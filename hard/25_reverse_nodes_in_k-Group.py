'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
---------------
speed
O(n)

memory
O(1)
'''


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = jump = ListNode(0)
        result.next = left = right = head

        while True:
            j = 0

            while right and j < k:
                right = right.next
                j += 1

            if j == k:
                previous, current = right, left
                
                for _ in range(k):
                    temp = current.next
                    current.next = previous
                    previous = current
                    current = temp
                
                jump.next = previous
                jump = left
                left = right

            else:
                return result.next

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution().reverseKGroup(l, 3)

while solution:
    print(solution.val)
    solution = solution.next