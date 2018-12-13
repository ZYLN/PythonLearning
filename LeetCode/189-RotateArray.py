class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # k %= len(nums)
        # while k > 0:
        #     a = nums.pop()
        #     nums.insert(0, a)
        #     k -= 1
        # return nums
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        # return nums
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

s = Solution()
print(s.rotate([1,2,3,4,5,6,], 2))