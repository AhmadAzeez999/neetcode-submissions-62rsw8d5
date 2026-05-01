class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lPtr = 0
        countMap = {}
        res = 0
        for rPtr in range(len(s)):
            countMap[s[rPtr]] = 1 + countMap.get(s[rPtr], 0)

            while ((rPtr - lPtr + 1) - max(countMap.values())) > k:
                countMap[s[lPtr]] -= 1
                lPtr += 1 

            res = max(res, rPtr - lPtr + 1)
        return res