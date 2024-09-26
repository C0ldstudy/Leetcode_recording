# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        length = len(val_list) // 2
        for i in range(length):
            if val_list[i] != val_list[-i-1]: return False
        return True
            
        