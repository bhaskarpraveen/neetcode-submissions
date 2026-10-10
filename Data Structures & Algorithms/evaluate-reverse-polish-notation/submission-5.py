class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop()  + stack.pop())
            elif token == '-':
                f = stack.pop()
                s = stack.pop()
                stack.append(s-f)
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token =='/':
                f = stack.pop()
                s = stack.pop()
                stack.append(int(float(s)/f))
            else:
                stack.append(int(token))
        return stack[0]

                 