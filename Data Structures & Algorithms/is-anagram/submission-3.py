class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        for c in s:
            ds[c] = ds.get(c, 0) + 1
        dt = {}
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        d_iter, d_other = (ds, dt) if len(ds) >= len(dt) else (dt, ds)
        for k, n in d_iter.items():
            if d_other.get(k, -1) != n:
                return False
        return True


