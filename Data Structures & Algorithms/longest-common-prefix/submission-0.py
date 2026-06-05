class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ''
        for i, char in enumerate(strs[0]):
            if all(len(word) > i and word[i] == char for word in strs):
                final += char
            else:
                break
        return final
        