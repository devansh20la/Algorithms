class Solution:
    def decodeString(self, s: str) -> str:
        countstack = []
        stringstack = []
        k = 0
        currentstring = ""
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                countstack.append(k)
                stringstack.append(currentstring)
                currentstring = ""
                k = 0
            elif c == ']':
                decodedstring = currentstring*countstack.pop()
                currentstring = stringstack.pop() + decodedstring
            else:
                currentstring += c

        return currentstring