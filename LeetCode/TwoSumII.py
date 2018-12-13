class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #双指针法，两端向中间靠拢
        left = 0
        right = len(numbers) - 1
        res = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                res.append(left)
                res.append(right)
                return res
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return res

s = Solution()
print(s.twoSum([2,7,11,15], 9))