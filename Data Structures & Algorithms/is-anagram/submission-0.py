from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #figure out if their freq map matches
        # two freq dictionaries return if they match (n+m space 1 time)
        # go through one string and search for the other character in the other removing once found (n^2. 1 space)
        # sort characters and then return if the strings are the same (nlogn time, 1 space)
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for s_char in s:
            s_freq[s_char] += 1
        for t_char in t:
            t_freq[t_char] +=1
        return s_freq == t_freq
            