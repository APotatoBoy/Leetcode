class Solution:
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        if i >= j:
            return True
    def partition(self,s):
        length = len(s)
        if length == 1:
            return list(s)
