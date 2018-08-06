# encoding = utf-8


class Solution:
    def generate(self, numsRows):
        """
        generate the first numsRows of Pascal's triangle
        :param numsRows: int
        :return: List[List[int]]
        """
        lis0 = [1]
        lis1 = [1, 1]
        res = []
        temp = []
        if numsRows == 0:
            return []
        if numsRows == 1:
            return [[1]]
        if numsRows == 2:
            return [[1], [1,1]]
        res.append(lis0)
        res.append(lis1)
        for i in range(2, numsRows):
            temp.clear()
            temp.append(1)
            for index in range(1, i):
                temp.append(res[i - 1][index - 1] + res[i - 1][index])
            temp.append(1)
            res.append(temp[:])
        return res


numsRows = 5
res = Solution().generate(numsRows)
print(res)

