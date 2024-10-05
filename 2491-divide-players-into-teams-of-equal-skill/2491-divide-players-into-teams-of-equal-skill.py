class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = skill[0]+skill[-1]
        ans = skill[0]*skill[-1]
        for i in range(1, len(skill)//2):
            if check == (skill[i] + skill[-i-1]):
                ans += skill[i] * skill[-i-1]
            else:
                return -1
        return ans