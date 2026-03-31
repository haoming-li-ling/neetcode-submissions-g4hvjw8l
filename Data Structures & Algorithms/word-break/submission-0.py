class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = [True] + [False] * len(s)
        scanned = ""
        for i, c in enumerate(s):
            index = i + 1
            scanned += c
            for w in wordDict:
                if len(w) > len(scanned):
                    continue
                suffix = True
                for i, (cw, cs) in enumerate(zip(reversed(w), reversed(scanned))):
                    if cw != cs:
                        suffix = False
                        break
                if suffix:
                    if m[index - len(w)]:
                        m[index] = True
                        break
        return m[len(s)]

        