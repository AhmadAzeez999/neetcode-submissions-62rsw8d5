class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minStr = ""
        minLen = float("inf")

        if len(t) > len(s): return minStr

        tMap = {}
        window = {}

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        l = 0
        have, need = 0, len(tMap)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tMap and tMap[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    minStr = s[l:r+1]
                    minLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        return minStr