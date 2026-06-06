class Solution:
    def isValid(self, s: str) -> bool:
        opening = ('(', '{', '[')
        closing = (')', '}', ']')
        
        stack = deque()
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if (popped == '(' and c != ')') or (popped == '[' and c != ']') or (popped == '{' and c != '}'):
                    return False

        return len(stack) == 0
