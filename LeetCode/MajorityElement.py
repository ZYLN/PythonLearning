class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #正常算法
        # d = {}
        # total = int(len(nums) / 2)
        # for i, v in enumerate(nums):
        #     if v in d:
        #         d[v] += 1
        #     else:
        #         d[v] = 1
        # for k, v in d.items():
        #     if v > total:
        #         return k

        #摩尔投票法
        num = nums[0]
        count = 1
        for i, v in enumerate(nums[1:]):
            if num == v:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    num = v
        return num

s = Solution()
print(s.majorityElement([1,2,2,1,1,2,2]))
