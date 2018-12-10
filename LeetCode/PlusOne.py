class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(v) for i, v in enumerate(str(int(''.join(str(i) for i in digits)) + 1))]

s = Solution()
print(s.plusOne([1,2,3]))