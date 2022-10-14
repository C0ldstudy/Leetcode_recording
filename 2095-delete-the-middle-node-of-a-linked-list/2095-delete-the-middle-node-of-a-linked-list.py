# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return 
        dummy1 = dummy = head
        length = 0
        while dummy != None:
            length += 1
            dummy = dummy.next
        target = int(length/2)
        for i in range(target-1):
            dummy1 = dummy1.next
        dummy1.next = dummy1.next.next
        return head

        