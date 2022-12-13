### 4. Median of Two Sorted Arrays
Given two sorted arrays `nums1` and `nums2` of size m and n respectively, return **the median** of the two sorted arrays.
The overall run time complexity should be `O(log (m+n))`.

### Key idea
- check the special cases like one list is empty.
- use a heap to keep the most close two numbers since the median could need to use one or two middle numbers.


### Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m < n: return self.findMedianSortedArrays(nums2, nums1) # assume nums1 is longer than nums2
        if n == 0:
            if m == 1: return nums1[0]
            if m % 2 == 0:
                return float(nums1[int(m/2)]+nums1[int(m/2)-1])/2.0
            else:
                return float(nums1[int(m/2)])
        if m+n == 2: return (nums1[0]+nums2[0])/2.0
        temp = [0,0]
        middle = int((m+n)/2)
        current = 0
        m_index = 0
        n_index = 0
        while (current <= middle):
            print(current, m_index, n_index, temp)
            if (n_index == n):
                temp.pop(0)
                temp.append(nums1[m_index])
                m_index += 1
                current += 1
            elif (m_index == m):
                temp.pop(0)
                temp.append(nums2[n_index])
                n_index += 1
                current += 1
            elif (nums1[m_index]<=nums2[n_index]):
                temp.pop(0)
                temp.append(nums1[m_index])
                m_index += 1
                current += 1
            elif (nums1[m_index]>nums2[n_index]):
                temp.pop(0)
                temp.append(nums2[n_index])
                n_index += 1
                current += 1
        # print(current, m_index, n_index, temp)
        if (m+n) % 2 == 0:
            return float(temp[0]+temp[1])/2.0
        else:
            return float(temp[1])
```
