### 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Key: Calculate the sum of two numbers digit by digit. Be careful about the special situations.

### Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        higher = 0
        dummy = result = ListNode()
        while (l1 != None) & (l2 != None):
            digit_sum = l1.val + l2.val + higher
            if digit_sum > 9:
                higher = 1
                digit_sum -= 10
            else:
                higher = 0
            print(digit_sum, "ttt")
            dummy.next = ListNode(digit_sum, None)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while (l1 == None) & (l2 != None):
            if higher != 0:
                digit_sum = l2.val + higher
                if digit_sum > 9:
                    higher = 1
                    digit_sum -= 10
                else:
                    higher = 0
                dummy.next = ListNode(digit_sum, None)
            else:
                dummy.next = l2
            # print("l2: ", digit_sum)

            dummy = dummy.next
            l2 = l2.next
        while (l2 == None) & (l1 != None):
            # print(l1.val, higher)
            if higher != 0:
                digit_sum = l1.val + higher
                if digit_sum > 9:
                    higher = 1
                    digit_sum -= 10
                else:
                    higher = 0
                dummy.next = ListNode(digit_sum, None)
            else:
                dummy.next = l1
            # print("l1: ", digit_sum)
            dummy = dummy.next
            l1 = l1.next
        if higher == 1:
            dummy.next = ListNode(1, None)
        return result.next
```


### Script
```python
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        higher = 0
        dummy = result = ListNode()
        while (l1 != None) & (l2 != None):
            digit_sum = l1.val + l2.val + higher
            if digit_sum > 9:
                higher = 1
                digit_sum -= 10
            else:
                higher = 0
            print(digit_sum, "ttt")
            dummy.next = ListNode(digit_sum, None)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while (l1 == None) & (l2 != None):
            if higher != 0:
                digit_sum = l2.val + higher
                if digit_sum > 9:
                    higher = 1
                    digit_sum -= 10
                else:
                    higher = 0
                dummy.next = ListNode(digit_sum, None)
            else:
                dummy.next = l2
            # print("l2: ", digit_sum)

            dummy = dummy.next
            l2 = l2.next
        while (l2 == None) & (l1 != None):
            # print(l1.val, higher)
            if higher != 0:
                digit_sum = l1.val + higher
                if digit_sum > 9:
                    higher = 1
                    digit_sum -= 10
                else:
                    higher = 0
                dummy.next = ListNode(digit_sum, None)
            else:
                dummy.next = l1
            # print("l1: ", digit_sum)
            dummy = dummy.next
            l1 = l1.next
        if higher == 1:
            dummy.next = ListNode(1, None)
        return result.next

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

test = Solution()
l1 = lst2link([1,8])
l2 = lst2link([0])

result = test.addTwoNumbers(l1, l2)
while result != None:
    print(result.val)
    result = result.next
```
