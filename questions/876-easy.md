### 876. Middle of the Linked List

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second middle node**.

### Key insight
Get the length of the linked list and return the middle.


### Solution
My first solution is straightforward.
```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        temp = head
        length = 0
        while temp.next != None:
            length += 1
            temp = temp.next
        index = ceil(length/2)
        for i in range(index):
            result = result.next
        return result

```
So a better way is to use two pointer with double speed.

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while (fast != None) and (fast.next != None) :
            fast = fast.next.next
            slow = slow.next
        return slow
```

Another method is to convert pointer to array:
```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]
```
