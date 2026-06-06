class Solution:
    def encode(self, strs: List[str]) -> str:
        text = ""
        if strs:
            for i, s in enumerate(strs):
                if i != len(strs) - 1:
                    text += f'{s}é'
                else:
                    text += s
        else:
            text = "EMPTY_LIST"
        return text

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST":
            return []
        else:
            return s.split('é')