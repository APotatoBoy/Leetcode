# encoding = utf-8


class Solution:
    def isPalindrome(self, s):
        """
        judging whether a string is a palindrome
        :param s: str
        :return: bool
        """
        if len(s) == 0:
            return True
        s = s.lower()
        start = 0
        end = len(s) - 1
        while end > start:
            if s[start] == ' ' or (not s[start].isalnum()):
                start += 1
                continue
            if s[end] == ' ' or (not s[end].isalnum()):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


s = "A man, a plan, a canal: Panama"
res = Solution().isPalindrome(s)
print(res)