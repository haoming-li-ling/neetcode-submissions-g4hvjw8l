class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        m = [0] * N
        m[N - 1] = 1 if s[N - 1] != "0" else 0
        for i, c in enumerate(reversed(s)):
            if i == 0:
                continue
            index = len(s) - 1 - i #s[index] = c
            if c == "0":
                m[index] = 0
                continue
            m[index] += m[index + 1]
            if int(c + s[index + 1]) <= 26:
                if index + 2 <= N - 1:
                    m[index] += m[index + 2]
                else:
                    m[index] += 1
        return m[0]

        