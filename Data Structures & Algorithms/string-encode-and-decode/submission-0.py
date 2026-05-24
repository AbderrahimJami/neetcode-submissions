class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        for s in strs:
            s = f"{len(s)}#{s}"
            str += s
        return str
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # you have found a delimiter
            w = int(s[i:j])
            res.append(s[j+1:j+1+w])
            i = j+1+w
        return res