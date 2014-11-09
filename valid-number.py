# Link: https://oj.leetcode.com/problems/valid-number/
class Solution:
    """
    Notes please see https://blog.xiaoba.me/2014/11/10/leetcode-valid-number.html
    """
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        stateTable = [
            [ 1, 1, 1, 3, 3, 7, 7, 7,-1],
            [ 4, 3, 4,-1,-1,-1,-1,-1,-1],
            [ 0, 8,-1, 8,-1,-1,-1, 8, 8],
            [-1, 5,-1, 5,-1,-1,-1,-1,-1],
            [ 2,-1,-1,-1,-1, 6,-1,-1,-1]
        ]
        i = 0
        state = 0
        while True:
            if i == len(s):
                break
            c = s[i]
            i += 1
            inputType = self._getInputType(c)
            if inputType is None:
                return False
            state = stateTable[inputType][state]
            if state == -1:
                return False

        return state == 1 or state == 3 or state == 7 or state == 8

    def _isDigit(self, c):
        return c >= '0' and c <= '9'

    def _getInputType(self, c):
        if self._isDigit(c):
            return 0
        if c == '.':
            return 1
        if c == ' ':
            return 2
        if c.lower() == 'e':
            return 3
        if c == '+' or c == '-':
            return 4
