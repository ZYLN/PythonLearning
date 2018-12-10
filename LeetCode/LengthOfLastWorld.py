class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')[::-1]
        for i, v in enumerate(l):
            if v != '':
                return len(v)
        return 0
s = Solution()
print(s.lengthOfLastWord('a  '))