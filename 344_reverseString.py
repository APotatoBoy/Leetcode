class Solution:
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        #while i < j:
        #    s[i], s[j] = s[j], s[i]
        #    i += 1
        #    j -= 1
        s = s[::-1]

s = ['h','e','l','l','o']
Solution().reverseString(s)
print(s)