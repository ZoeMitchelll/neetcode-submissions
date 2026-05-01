class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        delimiter = "Z"
        for word in strs:
            ret+=str(len(word))+delimiter+word
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        delimiter = "Z"
        word_length = ""
        ret = []
        ndx = 0
        while ndx < len(s):
            character = s[ndx]
            print(ndx, character, character.isdigit(), character == 'Z')
            if character.isdigit():
                word_length+=character
                ndx += 1
            else:
                ret.append(s[ndx+1:ndx+int(word_length)+1])
                ndx = ndx+int(word_length)+1
                word_length = ""
        return ret



