class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = 0
        abbr_idx = 0
        while (word_idx < len(word)) and (abbr_idx < len(abbr)):
            if not abbr[abbr_idx].isdigit():
                if word[word_idx] == abbr[abbr_idx]:
                    word_idx += 1
                    abbr_idx += 1
                else:
                    return False
            else:
                number = ""
                while abbr[abbr_idx].isdigit():
                    # print(abbr_idx)
                    number += abbr[abbr_idx]
                    abbr_idx += 1
                    if abbr_idx >= len(abbr): break
                if number[0] == '0': return False
                word_idx += int(number)
        if (word_idx == len(word)) and (abbr_idx == len(abbr)): return True
        return False
            
        