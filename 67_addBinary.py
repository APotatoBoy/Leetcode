# encoding  = utf-8

class Solution:
    def addBinary(self, a, b):
        """
        Return the sum of two binary strings
        :param a: str
        :param b: str
        :return: str
        """
        length_a = len(a)
        length_b = len(b)
        if length_a > length_b:
            maxLength = length_a
            b = '0' * (maxLength - length_b) + b
        else:
            maxLength = length_b
            a = '0' * (maxLength - length_a) + a
        # a = '0' * (32 - length_a) + a
        # b = '0' * (32 - length_b) + b
        carry = 0
        res = ''
        for i in range(-1, -1 * maxLength - 1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            if sum == 3:
                res = str(1) + res
                carry = 1
            elif sum == 2:
                res = str(0) + res
                carry = 1
            else:
                res = str(sum) + res
                carry = 0
        if carry == 1:
            res = '1' + res
        index = res.find('1')
        if index == -1:
            return '0'
        else:
            return res[index:len(res)]


a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
res = Solution().addBinary(a, b)
print(res)
