class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = m
        b = n
        i = 0
        while b != 0:
            if a != 0 and nums1[a - 1] > nums2[b - 1]:
                nums1[m + n - i - 1] = nums1[a - 1]
                a -= 1
            else:
                nums1[m + n - i - 1] = nums2[b - 1]
                b -= 1
            i += 1
        return nums1

s = Solution()
print(s.merge([2,0], 1, [1], 1))