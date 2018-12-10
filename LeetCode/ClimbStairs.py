class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # import math
        # cnt = 1
        # for i in range(1, int(n / 2) + 1):  #排列组合
        #     cnt += math.factorial(n-i) / (math.factorial(i) * math.factorial(n - 2 * i))
        # return int(cnt)

        # if n == 1:        #斐波那契数列，递归法，会超时
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n == 1:  # 斐波那契额数列，循环法
            return 1
        if n == 2:
            return 2
        sum1 = 1
        sum2 = 2
        sum = 2
        for i in range(3, n + 1):
            sum = sum1 + sum2
            sum1 = sum2
            sum2 = sum
        return sum


s = Solution()
print(s.climbStairs(4))