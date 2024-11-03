class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        char_map = {}
        for i,c in enumerate(s):
            if c not in char_map:
                char_map[c] = []
            char_map[c].append(i)
        result = []
        
        for left, right in queries:
            count = 0
            
            for positions in char_map.values():
                left_bound = bisect_left(positions, left)
                right_bound = bisect_right(positions, right)
                # print(left_bound, right_bound, positions, left, right)
                num = right_bound - left_bound
                
                count += num * (num +1) //2
            result.append(count)
        return result