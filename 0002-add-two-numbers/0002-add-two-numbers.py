# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        stack = [head]
        while stack:
            node = stack.pop()
            node.val = l1.val + l2.val
            if l1.next and l2.next:
                node.next = ListNode()
                stack.append(node.next)
                l1 = l1.next
                l2 = l2.next
            elif l1.next:
                node.next = l1.next
                # return dummy
                break
            else:
                node.next = l2.next
                # return dummy
                break
        
        head = dummy
        # print(head)
        while head:
            if head.val > 9 :
                head.val = head.val % 10
                if head.next:
                    head.next.val += 1
                else:
                    head.next = ListNode()
                    head.next.val = 1
            head = head.next
           
        
        return dummy

        