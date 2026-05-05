class Solution:
    def isPalindrome(self, s: str) -> bool:
        #iterate through it backward/foward make 2 strings only alpha num and compare On On
        #two pointer iterate through it and make sure they match
        

        l = 0
        r = len(s) - 1
        while l < len(s) and r > 0:
            l_valid = s[l].isalnum()
            r_valid = s[r].isalnum()
            if l_valid and r_valid:
                if s[l].casefold() != s[r].casefold():
                    return False
                else:
                    l = l+1
                    r = r-1
            if not l_valid:
                l = l+1
            if not r_valid:
                r = r-1
        return True

        