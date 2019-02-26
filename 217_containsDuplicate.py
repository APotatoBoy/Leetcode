class Solution:
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1
        return False

nums = [1, 4, 2, 3]
print(Solution().containsDuplicate(nums))