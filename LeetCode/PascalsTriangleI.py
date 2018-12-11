class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        l = [[1]]
        for i in range(2, numRows+1):
            r = [1]
            for j in range(1, i):
                if j == i - 1:
                    r.append(l[i-2][i-2])
                else:
                    r.append(l[i-2][j-1] + l[i-2][j-0])
            l.append(r)
        return l
s = Solution()
print(s.generate(5))