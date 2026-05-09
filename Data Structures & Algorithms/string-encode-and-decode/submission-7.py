class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        length = ''
        while i < len(s):
            if s[i] == '#':
                length = int(length)
                if length == 0:
                    strs.append('')
                    i+= 1
                else:
                    strs.append(s[i+1:(i+1+length)])
                    i+= length + 1
                length = ''
            else:
                length += s[i]
                i+= 1

        return strs