### Question 19: Remove Nth Node From End of List

Question: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Key: Use two pointers with the fixed length (n) to

Solution:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
```
