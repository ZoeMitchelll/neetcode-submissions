class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')','{':'}','[':']'}
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                last_opened = stack.pop()
                if brackets[last_opened] != c:
                    return False
        return not stack