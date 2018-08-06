# encoding = utf-8

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        merge two sorted integer arrays
        :param nums1: List[int]
        :param m: int
        :param nums2:List[int]
        :param n: int
        :return: nothing
        """
        index_nums1 = 0
        index_nums2 = 0
        index_res = 0
        res = []
        while index_nums1 < m and index_nums2 < n:
            if nums1[index_nums1] < nums2[index_nums2]:
                res.append(nums1[index_nums1])
                index_nums1 += 1
            else:
                res.append(nums2[index_nums2])
                index_nums2 += 1
        if index_nums1 == m:
            for i in range(index_nums2, n):
                res.append(nums2[i])
        if index_nums2 == n:
            for i in range(index_nums1, m):
                res.append(nums1[i])

        for i in range(m + n):
            nums1[i] = res[i]


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)