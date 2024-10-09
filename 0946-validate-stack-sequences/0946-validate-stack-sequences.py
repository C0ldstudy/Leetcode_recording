class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0
        push_idx = 0
        while (pop_idx < len(popped)) or (push_idx < len(pushed)):
            # print(stack, pop_idx, push_idx)
            if popped[pop_idx] in stack:
                if popped[pop_idx] == stack[-1]:
                    stack.pop(-1)
                    pop_idx += 1
                else:
                    return False
            else:
                stack.append(pushed[push_idx])
                push_idx += 1
        return True