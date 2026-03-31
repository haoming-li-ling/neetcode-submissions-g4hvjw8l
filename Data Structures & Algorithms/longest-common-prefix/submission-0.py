class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for cs in zip(*strs):
            cf = cs[0]
            same = True
            for i in range(1, len(cs)):
                if cs[i] != cf:
                    same = False
                    break
            if same:
                prefix += cf
            else:
                break
        return prefix



        