class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check_list = [0] * 26
        for i in sentence:
            num = ord(i) - ord('a')
            check_list[num] = 1
        if sum(check_list) == 26:
            return True
        else:
            return False
            