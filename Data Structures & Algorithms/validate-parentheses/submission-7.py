class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        flag = True
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if stack and stack[-1] == dic[ch]:
                    stack.pop()
                else:
                    flag = False
                    break

        return not stack and flag

        