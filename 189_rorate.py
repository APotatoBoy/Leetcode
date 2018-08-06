#encoding=utf-8
class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        k = k % length
        temp = nums.copy()
        for i in range(k):
            nums[i] = temp[length + i - k]
        index = 0
        for j in range(k, length):
            nums[j] = temp[index]
            index += 1
        #return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)