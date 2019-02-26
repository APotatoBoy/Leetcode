class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        x = [0] * 26
        y = [0] * 26
        for i in range(0, len(s)):
            x[ord(s[i]) - ord('a')] += 1
            y[ord(t[i]) - ord('a')] += 1
        for i in range(0, 26):
            if x[i] != y[i]:
                return False
        return True

s = 'anagram'
t = 'nagaram'
print(Solution().isAnagram(s, t))