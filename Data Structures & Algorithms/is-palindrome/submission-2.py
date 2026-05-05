class Solution:
    def isPalindrome(self, s: str) -> bool:
        #iterate through it backward/foward make 2 strings only alpha num and compare On On
        #two pointer iterate through it and make sure they match
        front = 0
        back = -1
        s = s.lower()
        while front < len(s) and back*-1 < len(s):
            while front < len(s) and not s[front].isalnum():
                front = front + 1
            while back*-1 < len(s) and not s[back].isalnum():
                back = back - 1
            if back*-1 < len(s) and front < len(s) and s[front] != s[back]:
                return False
            back = back - 1
            front = front + 1
        return True

        