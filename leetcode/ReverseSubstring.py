class Solution(object):
    def reverseParentheses(self, s):
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += c
        return stack.pop()
