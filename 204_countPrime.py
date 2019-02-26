import math
class Solution:
    def isPrime(self, n):
        '''
        Judging whether a integer number is a prime number
        :param n:int
        :return : bool
        '''
        if(n <= 1):
            return False
        if n == 2 or n == 5:
            return True
        if n % 10 == 0 or (n % 10) % 2 == 0 or n % 10 == 5:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 :
                return False
        return True

    def countPrimes(self, n):
        '''
        以空间消耗换取时间消耗的原则，维护一个数组，每判断一个数，先查表，将该数的整数表置位合数
        :param n: int
        :return: int
        '''
        not_primes = [False]*n
        count = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if not not_primes[i]:
                j = i + i
                while j < n:
                    not_primes[j] = True
                    j += i
        for i in range(2, n):
            if not not_primes[i]:
                #print(i)
                count += 1
        return count


n = 1500000
#print(Solution().isPrime(n))
print(Solution().countPrimes(n))