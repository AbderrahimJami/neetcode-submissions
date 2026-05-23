class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for word in s:
            freq[word] = freq.get(word, 0) + 1
        for word in t:
            freq[word] = freq.get(word, 0) - 1
        return all(v == 0 for v in freq.values())