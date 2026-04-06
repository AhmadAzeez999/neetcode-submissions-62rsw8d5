class Solution:
    def isPalindrome(self, s: str) -> bool:
        lPtr, rPtr = 0, len(s) - 1
        while lPtr < rPtr:
            while lPtr < rPtr and not self.isAlNum(s[lPtr]):
                lPtr += 1
            while rPtr > lPtr and not self.isAlNum(s[rPtr]):
                rPtr -= 1
            if s[rPtr].lower() != s[lPtr].lower():
                return False
            lPtr += 1
            rPtr -= 1
        return True

    def isAlNum(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))