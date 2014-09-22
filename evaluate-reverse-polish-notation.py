# Link: https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        """
        Use stack.
        An easy problem.
        Care about the accuracy !
        """
        import operator as op
        operators = {
            '+': op.add,
            '-': op.sub,
            '*': op.mul,
            '/': op.div
            }
        stack = [];
        for t in tokens:
            if t in operators:
                a = float(stack.pop())
                b = float(stack.pop())
                val = operators[t](b, a)  # should use if-else things instead
                stack.append(int(val))
            else:
                stack.append(t)
        return int(stack[0])
