#encoidng = utf-8
class Solution:
    def majorityElement(self, nums):
        """
        :param nums:
        :return: the majority of list nums
        """
        length = len(nums)
        count = []
        index = 0
        nums.sort()
        return nums[(int)(length/2)]

nums = [1, 2, 1, 2, 1]
sol = Solution().majorityElement(nums)
print(sol)
