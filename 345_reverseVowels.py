class Solution:
    def reverseVowels(self,s):
        vowel = ['a','A','e','E','i','I','o','O','u','U']
        list_s = list(s)
        i = 0
        j = len(list_s) - 1
        while i < j:
            if list_s[i] in vowel and list_s[j] in vowel:
                list_s[i],list_s[j] = list_s[j],list_s[i]
                i += 1
                j -= 1
            elif list_s[i] in vowel:
                j -= 1
            elif list_s[j] in vowel:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(list_s)

s = 'leetcode'
print(Solution().reverseVowels(s))