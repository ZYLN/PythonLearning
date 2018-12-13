class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # if len(nums1) < (m + n):
        #     return False
        # cout = 0
        # index = 0
        # for i in range(n):
        #     j = index
        #     if j < (m +cout):
        #         if nums1[j] < nums2[i]:
        #             j += 1
        #         else:
        #             nums1.insert(j, nums2[i])
        #             index = j
        #             cout += 1
        #             j = m + cout
        #     else:
        #         nums1[j:] = nums2[i:]
        # return nums1
        try:
            count = 0
            i = 0
            j = 0
            while i < n and j < (m + count):
                if nums1[j] < nums2[i]:
                    j += 1
                else:
                    nums1.insert(j, nums2[i])
                    i += 1
                    j += 1
                    count += 1
            else:
                if j == (m+count):
                    nums1[j:] = nums2[i:]
                    nums1 = nums1[:(m+n)]
                    print(nums1)
                    # return nums1 #这个程序没有返回值，把返回值去掉
                else:
                    nums1[:] = nums1[:(m + n)]
                    print(nums1)
                    # return nums1 #这个程序没有返回值，把返回值去掉
        except:
            return False

s = Solution()
nums11 =  [2,0]
m = 1
nums2 = [1]
n = 1
# print(s.merge(nums1, m, nums2, n))#打印方式不能用这种

s.merge(nums11, m, nums2, n)
print(nums11)

# method 2
# nums1[m:(m+n)] = nums2[:n]
# nums1.sort()
