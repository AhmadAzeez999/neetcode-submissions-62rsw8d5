class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s  
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            ptr = index

            while s[ptr] != ":":
                ptr += 1
            length = int(s[index:ptr])
            res.append(s[ptr + 1 : ptr + 1 + length])
            index = ptr + 1 + length
        return res


