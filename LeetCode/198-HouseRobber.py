class Solution:
    # def __init__(self):       #备忘录法
    #     self.d = {}
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lens = len(nums)      #备忘录法
        # if lens in self.d:
        #     return self.d[lens]
        # if lens == 0:
        #     sum = 0
        # elif lens == 1:
        #     sum = nums[0]
        # elif lens == 2:
        #     sum = nums[0] if nums[0] > nums[1] else nums[1]
        # else:
        #     sum = max(self.rob(nums[:-2]) + nums[lens - 1], self.rob(nums[:-1]))
        # self.d[lens] = sum
        # return sum

        lens = len(nums)        #DP法，动态规划
        if lens == 0:
            return 0
        elif lens == 1:
            return nums[0]
        max_rob0 = nums[0]
        max_rob1 = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2, lens):
            max_temp = max_rob0
            max_rob0 = max_rob1
            max_rob1 = max(max_temp + nums[i], max_rob1)
        return max_rob1

print([i for i in range(2,2)])
s = Solution()
print(s.rob([7, 2, 3, 8]))