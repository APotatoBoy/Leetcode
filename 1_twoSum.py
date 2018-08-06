# encoding = utf-8

def twoSum(nums, target):
    """
    find two num from a list, whose sum equals to the target
    :param nums:List[int]
    :param target: int
    :return: two dimensions List or null
    """
    for i in range(len(nums)):
        res = target - nums[i]
        j = lookup(nums, res, i)
        if j > 0 and j < len(nums) and j != i:
            return [i, j]
    return


def lookup(lis, target, start):
    """
    find the index of the element target
    :param lis: List[int]
    :param target: int
    :param start:
    :return:if find, return the index, else return -1
    """
    for i in range(start + 1, len(lis)):
        if lis[i] == target:
            return i
    return -1


nums = [2, 7, 11, 15]
target = 9
lis = twoSum(nums, target)
print(lis)
# nums = row_input()