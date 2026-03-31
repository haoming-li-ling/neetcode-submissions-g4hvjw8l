class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = [(True, nums[0])]
        for i in range(1, len(nums)):
            last_robbed, max_prev = m[i - 1]
            if not last_robbed:
                m.append((True, max_prev + nums[i]))
            else:
                if i - 2 < 0:
                    max_prev_prev = 0
                else:
                    max_prev_prev = m[i - 2][1]
                m.append((max_prev_prev + nums[i] > max_prev, max(max_prev_prev + nums[i], max_prev)))
        return m[len(nums) - 1][1]
        
         