class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                op = token
                a,b = stack.pop(), stack.pop()

                if op == '+':
                    stack.append(a + b)
                elif op == '-':
                    stack.append(b - a)
                elif op == '*':
                    stack.append(a * b)
                elif op == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack.pop()
