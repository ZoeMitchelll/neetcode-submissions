class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        delimiter = "ZoezoeZoe"
        for word in strs:
            ret+=delimiter+str(len(word))+delimiter+word
        return ret

    def decode(self, s: str) -> List[str]:
        delimiter = "ZoezoeZoe"
        chunks = s.split(delimiter)
        ret = []
        print(chunks)
        ndx = 0
        while ndx < len(chunks):
            if chunks[ndx].isdigit():
                print(chunks[ndx])
                ret.append(chunks[ndx+1])
                ndx += 2
            else:
                ndx += 1
        return ret
