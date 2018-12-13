class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #传统方法，不能处理较大的值，应该不去算阶乘，直接得出结果
        # from functools import reduce
        # if n < 5:
        #     return 0
        # factorial = reduce(lambda x, y: x * y, range(1, n + 1))
        # count = 0
        # while factorial > 1:
        #     if factorial % 10 is not 0:
        #         return count
        #     factorial = int(factorial / 10)
        #     count += 1
        # return count
        total = 0
        while n > 0:
            n //= 5
            total += n
        return total

s = Solution()
print(s.trailingZeroes(32))
