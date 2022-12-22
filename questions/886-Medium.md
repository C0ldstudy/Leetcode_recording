### 886. Possible Bipartition
We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [ai, bi]` indicates that the person labeled `ai` does not like the person labeled `bi`, return `true` if it is possible to split everyone into two groups in this way.

### Key idea
- One main problem I met is that it is harder than a two color graph problem. So far I cannot direct deal with multiple graphes issue.
- I am thinking about deal with the multiple graphs issue at the very beginning.



### Solution
This algorithm cannot work if multiple unconnected graphs are in the same edge list.
```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        length = len(dislikes)
        if length <= 1: return True
        for i, e in enumerate(dislikes):
            dislikes[i] = [min(e), max(e)]
        dislikes = sorted(dislikes, key=lambda x:x[1])
        dislikes = sorted(dislikes, key=lambda x:x[0])
        node_dict = {1:True}
        print(dislikes)
        # back = []
        for edge in dislikes:
            # print(edge, node_dict)
            if not edge[0] in node_dict.keys():
                if edge[1] in node_dict.keys():
                    node_dict[edge[0]] =  not node_dict[edge[1]]
                else:
                    print(edge)
                    node_dict[edge[0]] = False
                    node_dict[edge[1]] = True

            elif node_dict[edge[0]] == True:
                if edge[1] in node_dict.keys():
                    if node_dict[edge[1]] != False:
                        return False
                else:
                    node_dict[edge[1]] = False
            elif node_dict[edge[0]] == False:
                if edge[1] in node_dict.keys():
                    if node_dict[edge[1]] != True:
                        return False
                else:
                    node_dict[edge[1]] = True


        # print(node_dict)
        return True
```

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in adj[node]:
                if color[neighbor] == color[node]: return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False

            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 0):
                    # Return false, if there is conflict in the component.
                    return False

        return True
```
