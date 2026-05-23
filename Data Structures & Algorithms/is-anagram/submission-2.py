class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {char: s.count(char) for char in set(s)}
        m_freq = {char: t.count(char) for char in set(t)}
        if len(s_freq) != len(m_freq):
            return False
        for word in s_freq:
            if word not in m_freq:
                return False
            if m_freq[word] != s_freq[word]:
                return False
        return True
