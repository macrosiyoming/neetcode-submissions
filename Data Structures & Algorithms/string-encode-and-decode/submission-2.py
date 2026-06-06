class Solution:
    def encode(self, strs: List[str]) -> str:
        text = ""
        for s in strs:
            text += str(len(s)) + '@' + s
        return text

    def decode(self, s: str) -> List[str]:
        text, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            text.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return text