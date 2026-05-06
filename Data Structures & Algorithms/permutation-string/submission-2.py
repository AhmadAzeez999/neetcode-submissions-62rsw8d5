class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Hashmap = {}
        windowHashmap = {}

        for c in s1:
            s1Hashmap[c] = s1Hashmap.get(c, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            windowHashmap[s2[r]] = windowHashmap.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                windowHashmap[s2[l]] -= 1
                if windowHashmap[s2[l]] <= 0: windowHashmap.pop(s2[l])
                l += 1

            print(windowHashmap)

            if s1Hashmap == windowHashmap:
                return True

        print(s1Hashmap)
        return False