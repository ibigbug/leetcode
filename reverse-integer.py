# Link: https://oj.leetcode.com/problems/reverse-integer/
class Solution:
    # @return an integer
    def reverse(self, x):
        s = str(x)
        minus = False
        if s.startswith('-'):
            minus = True
            s = s[1:]
        s = s[::-1]

        return -int(s) if minus else int(s)
