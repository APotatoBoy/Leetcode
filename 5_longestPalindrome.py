#encoding=utf-8
class Solution:
    def longestPalindrome(self, s):
        """
        find the longest palindromic substring in s.
        :param s:
        :return:longest palindrome substring
        """
        length = len(s)
        if length <= 1:
            return s
        maxLength = 0
        output = ""
        for i in range(length):
            x = 1
            # 奇数长度的回文串，如abcba
            while i - x >= 0 and i + x < length:
                if s[i - x] == s[i + x]:
                    x += 1
                else:
                    break
            x -= 1
            if maxLength  < 2 * x + 1:
                maxLength = 2 * x + 1
                output = s[i - x:i + x + 1]
            # 偶数长度回文串，如abba
            x = 0
            while i - x >= 0 and i + x + 1 < length:
                if s[i - x] == s[i + x + 1]:
                    x += 1
                else:
                    break
            x -= 1
            if maxLength < 2 * x + 2:
                maxLength = 2 * x + 2
                output = s[i - x:i + x + 2]

        return output

s = 'baab'
sol = Solution().longestPalindrome(s)
print(sol)

