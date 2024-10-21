class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): return self.gcdOfStrings(str2, str1)
        result = str2
        while result:
            if (str1 == result* (len(str1)//len(result))) and (str2 == result* (len(str2)//len(result))):
                return result
            else:
                result = result[:-1]
        return result
        