
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        #数组nums前i个（包括第i个）数的和
        self.sum = []
        temp = 0
        for i in range(0, len(nums)):
            temp += self.nums[i]
            self.sum.append(temp)

    def sumRange(self, i, j):
        if i == 0:
            return self.sum[j - i]
        else:
            return self.sum[j] - self.sum[i - 1]

nums = [-2, 0, 3, -5, 2, -1]
print(NumArray(nums).sumRange(0,2))
