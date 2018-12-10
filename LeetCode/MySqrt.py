class Solution:
    def mySqrt(self, a):
        """
        :type x: int
        :rtype: int
        """
        x = a
        y = 0.0
        while abs(x - y) > 0.00001:
            y = x
            x = 0.5 * (x + a / x)
        return int(x)


s = Solution()
print(s.mySqrt(8))