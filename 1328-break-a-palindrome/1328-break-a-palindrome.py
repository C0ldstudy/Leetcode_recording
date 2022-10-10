class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if (len(palindrome) < 2):
            return ''
        number = []
        for i in palindrome:
            if i != 'a':
                number.append(ord(i))
        # special case: 'aa'
        if len(number) < 2 :
            palindrome = palindrome[:-1] + 'b'
            return palindrome
        
        target = chr(number[0])
        # print(target)
        for i, cha in enumerate(palindrome):
            if target == cha:
                # palindrome[i] = 'a'
                palindrome = palindrome[:i] + 'a' + palindrome[(i+1):]

                # print(palindrome)
                return palindrome
        return ''