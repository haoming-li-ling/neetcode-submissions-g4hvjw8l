class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = [1] * len(nums)
        cur_l_g = 1
        for i in range(1, len(nums)):
            cur_l = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    if m[j] + 1 > cur_l:
                        cur_l = m[j] + 1
            if cur_l > cur_l_g:
                cur_l_g = cur_l
            m[i] = cur_l
        return cur_l_g


