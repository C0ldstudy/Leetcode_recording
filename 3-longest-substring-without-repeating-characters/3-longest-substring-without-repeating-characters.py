class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substring = []
        max_left, max_right = 0, 0
        for i in s:
            if not i in substring:
                substring += i
                right += 1
            else:
                
                substring = substring[1:]
                substring += i
                left += 1
                right += 1
                # print(left, right, substring, i)
                
                while i in substring[:-1]:
                    left += 1
                    substring = substring[1:]
            # print(left, right, substring, i)
            if (max_right - max_left) < (right-left):
                max_right = right
                max_left = left
        return max_right - max_left
                
            
            