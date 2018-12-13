class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #时间超限
        # return None if len(nums) == 0 else [v for i, v in enumerate(nums) if v not in nums[0: i] + nums[i + 1:]][0]
        #直接判断，效率较低
        # d = {}
        # for i, v in enumerate(nums):
        #     if v in d:
        #         d[v] += 1
        #     else:
        #         d[v] = 1
        # for k, v in d.items():
        #     if v == 1:
        #         return k
        #异或的用法
        result = 0
        for i, v in enumerate(nums):
            result ^= v
        return result

s = Solution()
print(s.singleNumber([2,2,1]))