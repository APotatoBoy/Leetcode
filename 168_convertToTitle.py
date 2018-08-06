# encoding = utf-8
import string
class Solution:
    def convertToTitle(self, Input):
        """
        Given a positive integer, return its corresponding column title as appear
        in an Excel sheet
        :param Input:int
        :return:str
        """
        if n < 0:
            return ''
        res = ''
        letter = ['Z']
        # print(letter. + 1)
        index = 0
        sol = ''
        for word in string.ascii_uppercase:
            letter.append(word)

        while Input > 0:
            if Input < 27:
                sol = letter[Input] + sol
                Input = 0
            else:
                sol_idx = (int)(Input % 26)
                if sol_idx == 0:
                    sol = letter[26] + sol
                    Input = Input - 1
                else:
                    sol = letter[sol_idx] + sol
                Input = int(Input / 26)

        return sol


n = 701
res = Solution().convertToTitle(n)
print(res)
