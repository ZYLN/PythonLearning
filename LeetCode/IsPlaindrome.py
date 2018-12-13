class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = [i.lower() for i in s if i.isalnum()]
        return l == l[::-1]

s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))