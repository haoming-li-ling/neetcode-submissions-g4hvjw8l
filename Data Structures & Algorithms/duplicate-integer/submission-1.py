class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for n in nums:
            if n not in d:
                d.add(n)
            else:
                return True
        return False

        