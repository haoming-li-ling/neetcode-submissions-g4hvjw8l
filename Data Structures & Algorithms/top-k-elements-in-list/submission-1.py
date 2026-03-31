class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = { i : set() for i in range(1, len(nums) + 1)}
        dd = {}
        for n in nums:
            dd[n] = dd.get(n, 0) + 1
        for n, c in dd.items():
            d[c].add(n)
        l = []
        for i in range(len(nums), -1, -1):
            for n in d.get(i, set()):
                l.append(n)
            if len(l) == k:
                break
        return l






        