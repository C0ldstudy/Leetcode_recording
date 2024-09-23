# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = dummy = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                merged_list.next = list2
                merged_list = merged_list.next
                list2 = list2.next
            else:
                merged_list.next = list1
                merged_list = merged_list.next
                list1 = list1.next
        if (not list1) and (not list2): return dummy.next
        if list1:
            merged_list.next = list1
        else:
            merged_list.next = list2
        return dummy.next
            
        