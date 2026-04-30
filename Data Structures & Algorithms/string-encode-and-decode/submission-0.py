class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        delimiter = "ZoezoeZoe"
        for word in strs:
            ret+=word+delimiter
        return ret

    def decode(self, s: str) -> List[str]:
        delimiter = "ZoezoeZoe"
        return s.split(delimiter)[:-1]
