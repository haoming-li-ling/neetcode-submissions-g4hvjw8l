class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None
        for n in nums:
            if count == 0:
                cand = n
            if n == cand:
                count += 1
                continue
            if n != cand:
                count -= 1
        return cand
            




