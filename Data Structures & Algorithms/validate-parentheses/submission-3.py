class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(': ')', '[': ']', '{': '}'}
        stack = deque()

        for c in s:
            if c in map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if map[popped] != c:
                    return False

        return len(stack) == 0
