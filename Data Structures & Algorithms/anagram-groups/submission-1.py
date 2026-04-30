from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary of a set mapped to a list and then for every string make a set of it and compare (time n*m space n)
        #sort every string and get the ndx of same strings and return the ndx of origional list grouped together (time nlogn+n space n)
        groups = defaultdict(list)
        for string in strs:
            freq = [0]*26
            for character in string:
                freq[ord(character) -97] = freq[ord(character) -97] + 1
            groups[tuple(freq)].append(string)
        return list(groups.values())
        