class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count = [0] * 26
        windowCount = [0] * 26

        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            windowCount[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) > len(s1):
                windowCount[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if windowCount == s1Count:
                return True
        return False
            