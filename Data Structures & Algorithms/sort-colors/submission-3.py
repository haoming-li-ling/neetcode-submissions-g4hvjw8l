class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightmost_zero = -1
        rightmost_one = -1
        one = False
        for i, n in enumerate(nums):
            if n == 1:
                nums[i], nums[rightmost_one + 1] = nums[rightmost_one + 1], nums[i]
                rightmost_one += 1
                one = True
            if n == 0:
                nums[rightmost_zero + 1], nums[i] = nums[i], nums[rightmost_zero + 1]
                if one:
                    nums[i] = nums[rightmost_one + 1]
                    nums[rightmost_one + 1] = 1
                rightmost_zero += 1
                rightmost_one += 1
        