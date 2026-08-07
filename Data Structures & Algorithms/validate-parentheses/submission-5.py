class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if map[popped] != char:
                    return False
        
        return len(stack) == 0

       
