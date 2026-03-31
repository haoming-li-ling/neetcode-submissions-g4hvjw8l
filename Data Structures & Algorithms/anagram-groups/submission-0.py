class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lg = []

        def to_dict(s):
            d = {}
            for c in s:
                d[c] = d.get(c, 0) + 1
            return d
        
        dd = {}
        for i, s in enumerate(strs):
            ds = to_dict(s)
            dd[s] = ds
            added = False
            for g in lg:
                dg = dd[g[0]]
                if dg == ds:
                    g.append(s)
                    added = True
                    break
            if not added:
                lg.append([s])
        return lg


        