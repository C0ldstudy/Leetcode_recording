### 1339. Maximum Product of Splitted Binary Tree

Given the `root` of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it **modulo** `10**9 + 7`.

Note that you need to maximize the answer before taking the mod and not after taking it.


### Key idea
- Leverage the sum of the whole elements
- Binary tree just contains distinguished elements.



### Solution

My original one exceeds the time limitation
```python
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.whole = self.sum_tree(root)
        self.max_val = 0
        def dfs(node):
            if node:
                result = self.sum_tree(node)
                self.max_val = max(self.max_val,result*(self.whole-result))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        self.max_val =  self.max_val % (10**9 + 7)
        return self.max_val

    def sum_tree(self, root):
        if (root == None): return 0
        return (root.val + self.sum_tree(root.left) + self.sum_tree(root.right))
```

A better one is to convert the max prodcut to find the result close to the half of the sum.

```python
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        subtreeSums = set()

        def getSum(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                subtreeSums.add(node.val)
                return node.val
            else:
                result = getSum(node.left) + getSum(node.right) + node.val
                subtreeSums.add(result) # what if there exists repeated elements? Binary tree does not allow duplicated keys!
                return result

        rootSum = getSum(root)
        idealSplit = rootSum/2
        closestToIdeal = 0

        for possibleSum in subtreeSums:
            if math.fabs(possibleSum - idealSplit) < math.fabs(closestToIdeal - idealSplit):
                closestToIdeal = possibleSum

        return (((rootSum - closestToIdeal) % (10**9 + 7)) * (closestToIdeal % (10**9 + 7)))  % (10**9 + 7)
```
