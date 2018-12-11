class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        rowIndex += 1
        l = [1]
        for i in range(2, rowIndex + 1):
            j = i - 2
            l.append(1)
            while j > 0:
                l[j] = l[j - 1] + l[j]
                j -= 1
        return l

s = Solution()
print(s.getRow(3))