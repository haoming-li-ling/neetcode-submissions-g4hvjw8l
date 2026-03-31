class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "."
        last = 0
        for s in strs:
            res = str(last) + "," + str(len(s)) +  ";" + res + s
            last += len(s)
        return res

    def decode(self, s: str) -> List[str]:
        hd, tl = s.split(".", 1)
        l = []
        for sn in reversed(hd.split(";")):
            if sn == "":
                continue
            start, length = sn.split(",")
            l.append(tl[int(start):int(start) + int(length)])
        return l
