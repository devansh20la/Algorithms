class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == ']':
                decoded_str = []
                p = stack.pop()
                while p != '[':
                    decoded_str.append(p)
                    p = stack.pop()
                
                count = []
                while len(stack) > 0  and stack[-1].isdigit():
                    count += [stack.pop()]
                count = int("".join(count[::-1]))
                decoded_str = decoded_str[::-1]*int(count)
                stack += decoded_str
            else:
                stack.append(c)
        
        return "".join(stack)