class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def recurse(stack):
            token = stack.pop()
            if token not in '+-*/':
                return int(token)
            
            right = recurse(stack)
            left = recurse(stack)

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return recurse(tokens)

        
