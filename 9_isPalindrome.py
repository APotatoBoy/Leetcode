# encoding = utf-8

class Solution:
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome
        In this method, the Integer inputted is changed into a string
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        length = len(x_str)
        start, end = 0, length - 1
        while start < end:
            if x_str[start] != x_str[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

    def isPalindrome2(self, x):
        """
        Determine whether an integer is a palindrome
        In this method, every digit of the integer inputted is stored in a list
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        x_lis = []
        tmp = x
        i = 0
        while tmp > 0:
            x_lis.append(tmp % 10)
            tmp = int(tmp / 10)
        start, end = 0, len(x_lis) - 1
        while start < end:
            if x_lis[start] != x_lis[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


x = 121212
sol = Solution()
y = sol.isPalindrome(x)
print(y)
y = sol.isPalindrome2(x)
print(y)