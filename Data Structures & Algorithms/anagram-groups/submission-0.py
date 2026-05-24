class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams.setdefault(sorted_word, []).append(word)
        return list(anagrams.values())

