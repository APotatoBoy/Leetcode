# encoding = utf-8


class Solution:
    def plusOne(self, digits):
        """
        plus one to the integer
        :param digits: List[int]
        :return:List[int]
        """
        s = ''
        for i in digits:
            s += str(i)
        num = int(s)
        num += 1
        s = str(num)
        for j in range(len(s)):
            if j < len(digits):
                digits[j] = int(s[j])
            else:
                digits.append(int(s[j]))
        return digits


digits = [9]
res = Solution().plusOne(digits)
print(res)
