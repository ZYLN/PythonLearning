class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum = nums[0]
        # lens = len(nums)
        # for i in range(1, lens+1):
        #     for j in range(lens - i + 1):
        #         sum_temp = 0
        #         for k in range(i):
        #             sum_temp += nums[j + k]
        #         if sum_temp > sum:
        #             sum = sum_temp
        # return sum
        lens = len(nums)
        sum = nums[0]
        maxnum = max(nums)
        for i in range(1, lens):
            if nums[i] < 0:
                sum += nums[i]
            else:
                if sum < 0:
                    sum = 0
                sum += nums[i]
                if maxnum < sum:
                    maxnum = sum
        return maxnum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(max([1,2]))