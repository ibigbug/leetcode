# Link: https://oj.leetcode.com/problems/valid-parentheses/
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        m = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if m.get(t, None) != c:
                    return False
        return len(stack) == 0
