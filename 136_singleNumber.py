# encoding = utf-8


class Solution:
    def singleNumber(self, nums):
        """
        find the single number of the given list
        %%attention: x ^ x = 0
        :param nums:List[int]
        :return:int
        """
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans


nums = [4, 1, 2, 1, 2]
res = Solution().singleNumber(nums)
print(res)