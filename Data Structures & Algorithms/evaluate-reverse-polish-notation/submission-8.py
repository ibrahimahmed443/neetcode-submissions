class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def recurse():
            token = tokens.pop()
            if token not in '+-*/':
                return int(token)
            
            right = recurse()
            left = recurse()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return recurse()

        
