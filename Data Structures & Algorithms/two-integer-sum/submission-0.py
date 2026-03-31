class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            prev = d.get(n, -1)
            if prev >= 0:
                return [prev, i]
            d[target - n] = i


        