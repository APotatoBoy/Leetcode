#encoding=utf-8
import math
class Solution:
    def myAtoi(self, s):
        """
        convert a string to an integer.
        :param s:input string
        :return:integer
        """
        length = len(s)
        it = 0
        start = 0
        #output = 0
        MAX = math.pow(2, 31) - 1
        MIN = math.pow(2, 31)  * (-1)
        while it < length and s[it] == ' ':
            it += 1
        if it == length:
            return 0
        if s[it] == '-' or s[it] == '+':
            outputBegin = it
            start = it + 1
            it += 1
        if s[it] >= '0' and s[it] <= '9':
            start = it
            outputBegin = it
        else:
            return 0
        for i in range(start, length):
            if s[i] >= '0' and s[i] <= '9':
                continue
            else:
                i -= 1
                break
        output = int(s[outputBegin:i + 1])
        return MAX if output > MAX else (MIN if output < MIN else output)

        # if output > MAX:
        #     return MAX
        # elif output < MIN:
        #     return MIN
        # else:
        #     return output

s = '  -42'
sol = Solution().myAtoi(s)
print(sol)

