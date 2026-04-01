class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s  
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            ptr = i
            while s[ptr] != ":":
                ptr += 1
            wordLen = int(s[i:ptr])
            word = s[ptr + 1 : ptr + 1 + wordLen]
            res.append(word)
            i = ptr + 1 + wordLen
        return res


